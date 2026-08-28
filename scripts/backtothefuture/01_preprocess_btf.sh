#!/bin/bash

# Paths
export data_folder=/nndb_teens/jure/MovieProject/bids_data
export stim_folder=/nndb_teens/jure/MovieProject/stimuli
export fs_folder=/nndb_teens/jure/MovieProject/bids_data/derivatives/freesurfer

# Maximum number of parallel jobs and threads
max_jobs=6
export OMP_NUM_THREADS=4

# Extract subject IDs dynamically from the bids_data folder
#subjects=$(ls -d $data_folder/sub-* | awk -F'/' '{print $NF}' | sed 's/sub-//' | sort -n)
#echo "The list of subjects to be preprocessed: ${subjects[@]}"
 #20 29

subjects="XXX"
echo "The list of subjects to be preprocessed: ${subjects[@]}"
# Run AFNI
for subject_id in $subjects; do

    (
      # Start timing
      start_time=$(date +%s)

      # Paths for outputs
      echo "Processing subject-$subject_id"
      subject_folder="$data_folder"/derivatives/sub-"$subject_id"/backtothefuture
      script_path="$subject_folder"/proc.sub-"$subject_id"
      output_path="$subject_folder"/output.proc.sub-"$subject_id"
      results_path="$subject_folder"/sub-"$subject_id".results

      # Create target directory if it does not exist
      if [ ! -d "$subject_folder" ]; then
          mkdir -p "$subject_folder"
          echo "Created directory $subject_folder"
      fi

      # Default input paths
      dsets=(
          "$data_folder/sub-${subject_id}/ses-001/func/sub-${subject_id}_ses-001_task-backtothefuture_run-001_bold.nii.gz"
          "$data_folder/sub-${subject_id}/ses-001/func/sub-${subject_id}_ses-001_task-backtothefuture_run-002_bold.nii.gz"
          "$data_folder/sub-${subject_id}/ses-001/func/sub-${subject_id}_ses-001_task-backtothefuture_run-003_bold.nii.gz"
      )
      blip_reverse="$data_folder/sub-${subject_id}/ses-001/fmap/sub-${subject_id}_ses-001_acq-func_dir-PA_run-001_epi.nii.gz"
      anat_path="$data_folder/derivatives/sub-${subject_id}/SSwarper/anatSS.sub-${subject_id}.nii.gz"
      anat_skull="$data_folder/derivatives/sub-${subject_id}/SSwarper/anatU.sub-${subject_id}.nii.gz"
      stim_file="$stim_folder/task-backtothefuture_condition-speech_run-all.1D"
      n_trs_remove="8 16 16"


      # Adjustments for non-standard subjects:
      # 4; run2 was paused 3 times, run3 missing some TRs
      # 7; run 1 paused, run 2 paused twice
      # 8; run1 was paused, run2 was paused, run 3 has some extra runs (only the last one should be used)
      # 14; stopped with 18min to go in run1 (scan continued for 2 TRs after pause)
      # 20; started and then restarted run1, run2 started with 4TRs in matlab already, paused run2 at 1281.53s (659.78TRs left) and 675.78TRs in the new EPI (second part of run2)
      # 22; stopped 2min to go in run1 (1256 TRs instead of 1360). reverse reference done in different position, after localiser because helmet had to be removed
      # 25; run2 is incomplete
      
      if [ "$subject_id" == "22" ]; then
          stim_file="$stim_folder/task-backtothefuture_condition-speech_run-sub-LF.1D"
      elif [ "$subject_id" == "25" ]; then
          stim_file="$stim_folder/task-backtothefuture_condition-speech_run-sub-ST.1D"
      
      elif [ "$subject_id" == "4" ]; then # run 2 has a lot of pauses but unclear how the data was acquired, alignment
          dsets=(
              "$data_folder/sub-4/ses-001/func/sub-4_ses-001_task-backtothefuture_run-001_bold.nii.gz"
              "$data_folder/sub-4/ses-001/func/sub-4_ses-001_task-backtothefuture_run-003_bold.nii.gz"
          )
          n_trs_remove="8 16" #should it be 16? i guess if we are keeping the same stimulus file, yes. makes it easier to compare to other run 3s
          stim_file="$stim_folder/task-backtothefuture_condition-speech_run-sub-MS.1D" 
      elif [ "$subject_id" == "7" ]; then #run 5 is too short to be processed (problem with band pass filtering) - ignore the final chunk.
          dsets=(
              "$data_folder/sub-7/ses-001/func/sub-7_ses-001_task-backtothefuture_acq-beforepause_run-001_bold.nii.gz"
              "$data_folder/sub-7/ses-001/func/sub-7_ses-001_task-backtothefuture_acq-afterpause_run-001_bold.nii.gz"
              "$data_folder/sub-7/ses-001/func/sub-7_ses-001_task-backtothefuture_acq-part1_run-002_bold.nii.gz"
              "$data_folder/sub-7/ses-001/func/sub-7_ses-001_task-backtothefuture_acq-part2_run-002_bold.nii.gz"
              #"$data_folder/sub-7/ses-001/func/sub-7_ses-001_task-backtothefuture_acq-part3_run-002_bold.nii.gz"
              "$data_folder/sub-7/ses-001/func/sub-7_ses-001_task-backtothefuture_run-003_bold.nii.gz"
          )
          n_trs_remove="8 16 16 15 16" #remove only 15 because movie was paused after the scanner and there would otherwise be a gap of approx 1TR between part1 and part2 in terms of movie
          stim_file="$stim_folder/task-backtothefuture_condition-speech_run-sub-TD.1D" 
      elif [ "$subject_id" == "8" ]; then 
          dsets=(
              "$data_folder/sub-8/ses-001/func/sub-8_ses-001_task-backtothefuture_acq-beforepause_run-001_bold.nii.gz"
              "$data_folder/sub-8/ses-001/func/sub-8_ses-001_task-backtothefuture_acq-afterpause_run-001_bold.nii.gz"
              "$data_folder/sub-8/ses-001/func/sub-8_ses-001_task-backtothefuture_acq-beforepause_run-002_bold.nii.gz"
              "$data_folder/sub-8/ses-001/func/sub-8_ses-001_task-backtothefuture_run-003_bold.nii.gz"
          )
          n_trs_remove="8 12 16 16"
          stim_file="$stim_folder/task-backtothefuture_condition-speech_run-sub-EH.1D" # no timestamps for afterpause run
      elif [ "$subject_id" == "14" ]; then # shorter run1
          dsets=(
              "$data_folder/sub-14/ses-001/func/sub-14_ses-001_task-backtothefuture_run-001_bold.nii.gz"
              "$data_folder/sub-14/ses-001/func/sub-14_ses-001_task-backtothefuture_run-002_bold.nii.gz"
              "$data_folder/sub-14/ses-001/func/sub-14_ses-001_task-backtothefuture_run-003_bold.nii.gz"
          )
          n_trs_remove="8 16 16"
          stim_file="$stim_folder/task-backtothefuture_condition-speech_run-sub-FM.1D" # no timestamps for afterpause run
          blip_reverse="$data_folder/sub-14/ses-001/fmap/sub-14_ses-001_acq-func_dir-PA_run-002_epi.nii.gz"
      elif [ "$subject_id" == "20" ]; then # something odd in run 2, hard to say what happened, ignore it
            dsets=(
              "$data_folder/sub-20/ses-001/func/sub-20_ses-001_task-backtothefuture_run-001_bold.nii.gz"
              "$data_folder/sub-20/ses-001/func/sub-20_ses-001_task-backtothefuture_acq-part2_run-002_bold.nii.gz"
              "$data_folder/sub-20/ses-001/func/sub-20_ses-001_task-backtothefuture_acq-part3_run-002_bold.nii.gz"
              "$data_folder/sub-20/ses-001/func/sub-20_ses-001_task-backtothefuture_run-003_bold.nii.gz"
          )
          n_trs_remove="8 12 0 16"
          stim_file="$stim_folder/task-backtothefuture_condition-speech_run-sub-SJ.1D" # no timestamps for afterpause run
      elif [ "$subject_id" == "29" ]; then
            dsets=(
              "$data_folder/sub-29/ses-001/func/sub-29_ses-001_task-backtothefuture_run-001_bold.nii.gz"
              "$data_folder/sub-29/ses-001/func/sub-29_ses-001_task-backtothefuture_run-002_bold.nii.gz"
              "$data_folder/sub-29/ses-001/func/sub-29_ses-001_task-backtothefuture_run-003_bold.nii.gz"
            )
          n_trs_remove="8 16 16"
          stim_file="$stim_folder/task-backtothefuture_condition-speech_run-sub-MB.1D"
      elif [ "$subject_id" == "32" ]; then #no fmap for run 2, use run 1 reverse
      	blip_reverse="$data_folder/sub-32/ses-001/fmap/sub-32_ses-001_acq-func_dir-PA_run-002_epi.nii.gz"

      elif [ "$subject_id" == "33" ]; then 
        stim_file="$stim_folder/task-backtothefuture_condition-speech_run-sub-BM.1D"

      elif [ "$subject_id" == "38" ]; then 
            # Remove last 3 TRs from afterpause run (sub-38)
            afterpause_in="$data_folder/sub-38/ses-001/func/sub-38_ses-001_task-backtothefuture_acq-afterpause_run-002_bold.nii.gz"

            deriv_func_dir="$data_folder/derivatives/trimmed/sub-38/ses-001/func"
            mkdir -p "$deriv_func_dir"

            afterpause_out="$deriv_func_dir/sub-38_ses-001_task-backtothefuture_acq-afterpausetrimmed_run-002_bold.nii.gz"

            nt=$(3dinfo -nt "$afterpause_in")
            last_tr=$((nt - 4))

            3dTcat -overwrite \
                -prefix "$afterpause_out" \
                "${afterpause_in}[0..${last_tr}]"

            dsets=(
              "$data_folder/sub-38/ses-001/func/sub-38_ses-001_task-backtothefuture_run-001_bold.nii.gz"
              "$data_folder/sub-38/ses-001/func/sub-38_ses-001_task-backtothefuture_acq-beforepause_run-002_bold.nii.gz"
              "$afterpause_out"
              "$data_folder/sub-38/ses-001/func/sub-38_ses-001_task-backtothefuture_run-003_bold.nii.gz"
          )
          n_trs_remove="8 16 16 16"
          stim_file="$stim_folder/task-backtothefuture_condition-speech_run-sub-38.1D" # no timestamps for afterpause run
        task-backtothefuture_condition-speech_run-all-sub-38
        elif [ "$subject_id" == "40" ]; then 
            dsets=(
              "$data_folder/sub-40/ses-001/func/sub-40_ses-001_task-backtothefuture_run-001_bold.nii.gz"
              "$data_folder/sub-40/ses-001/func/sub-40_ses-001_task-backtothefuture_run-002_bold.nii.gz"
              "$data_folder/sub-40/ses-001/func/sub-40_ses-001_task-backtothefuture_acq-beforepause_run-003_bold.nii.gz"
              "$data_folder/sub-40/ses-001/func/sub-40_ses-001_task-backtothefuture_acq-afterpause_run-003_bold.nii.gz"
          )
          n_trs_remove="8 16 16 16" #no need to adjust stim file as pause happened during credits and no events happen after the pause

      fi

      # Run afni_proc.py to create preproc script
      timestamp=$(date +%Y%m%d_%H%M%S)
      afni_proc.py \
          -subj_id "$subject_id" \
          -script "$script_path.$timestamp" \
          -out_dir "$results_path.$timestamp" \
          -dsets "${dsets[@]}" \
          -blocks tcat align tlrc volreg mask blur scale regress \
          -blip_reverse_dset "$blip_reverse" \
          -tcat_remove_first_trs $n_trs_remove \
          -radial_correlate_blocks tcat volreg \
          -copy_anat "$anat_path" \
          -anat_has_skull no \
          -anat_follower anat_w_skull anat "$data_folder/derivatives/sub-${subject_id}/SSwarper/anatU.sub-${subject_id}.nii.gz" \
          -anat_follower_ROI aaseg    anat "$fs_folder/sub-${subject_id}/SUMA/aparc.a2009s+aseg.nii.gz" \
          -anat_follower_ROI aeseg    epi  "$fs_folder/sub-${subject_id}/SUMA/aparc.a2009s+aseg.nii.gz" \
          -anat_follower_ROI fsvent   epi  "$fs_folder/sub-${subject_id}/SUMA/fs_ap_latvent.nii.gz" \
          -anat_follower_ROI fswm     epi  "$fs_folder/sub-${subject_id}/SUMA/fs_ap_wm.nii.gz" \
          -anat_follower_ROI fsgm     epi  "$fs_folder/sub-${subject_id}/SUMA/aparc+aseg_REN_gm.nii.gz" \
          -anat_follower_erode fsvent fswm \
          -align_opts_aea -cost lpc+ZZ -giant_move -check_flip \
          -tlrc_base MNI152_2009_template_SSW.nii.gz \
          -tlrc_NL_warp \
          -tlrc_NL_warped_dsets \
            "$data_folder/derivatives/sub-${subject_id}/SSwarper/anatQQ.sub-${subject_id}.nii.gz" \
            "$data_folder/derivatives/sub-${subject_id}/SSwarper/anatQQ.sub-${subject_id}.aff12.1D" \
            "$data_folder/derivatives/sub-${subject_id}/SSwarper/anatQQ.sub-${subject_id}_WARP.nii.gz" \
          -volreg_align_to MIN_OUTLIER \
          -volreg_post_vr_allin yes \
          -volreg_pvra_base_index MIN_OUTLIER \
          -volreg_align_e2a \
          -volreg_tlrc_warp \
          -volreg_opts_vr -twopass -twodup -maxdisp1D mm'.r$run' \
          -volreg_compute_tsnr yes \
          -mask_opts_automask -clfrac 0.10 \
          -mask_epi_anat yes \
          -blur_to_fwhm -blur_size 4 \
          -regress_motion_per_run \
          -regress_ROI_PC fsvent 3 \
          -regress_ROI_PC_per_run fsvent \
          -regress_make_corr_vols aeseg fsvent \
          -regress_anaticor_fast \
          -regress_anaticor_label fswm \
          -regress_apply_mot_types demean deriv \
          -regress_est_blur_epits \
          -regress_est_blur_errts \
          -regress_run_clustsim no \
          -regress_polort 2 \
          -regress_bandpass 0.01 1 \
          -regress_opts_3dD -num_stimts 1 -local_times \
              -stim_label 1 Speech \
              -stim_times_AM1 1 "$stim_file" 'dmUBLOCK(1)' \
          -regress_reml_exec \
          -remove_preproc_files \
          -html_review_style pythonic

      # execute preproc script
      tcsh -xef "$script_path.$timestamp" 2>&1 | tee "$output_path.$timestamp"

      # end timing
      end_time=$(date +%s)

      # Calculate elapsed time
      elapsed_time=$((end_time - start_time))
      echo "Processing time for subject $subject_id: ${elapsed_time} seconds"

      # Compress files for this subject
      echo "Compressing files for subject $subject_id..."
      find "$results_path.$timestamp" -type f \( -name "*.nii" -o -name "*.BRIK" \) -exec gzip -f "{}" \;
      echo "Compression for subject $subject_id completed."
    ) &

    # Limit the number of parallel jobs
    while [ "$(jobs -p | wc -l)" -ge "$max_jobs" ]; do
        sleep 10
    done
done

# Wait for all background jobs to finish
wait


### Useful links to understand the rationale of the analysis:
# ISC recommendations by Chen and Cox: https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/_downloads/s.2016_ChenEtal_02_ap.tcsh
# Polort and bandpassing: https://discuss.afni.nimh.nih.gov/t/afni-proc-regress-polort-option-for-very-long-runs/3487
# Blurring: Default blurring option is 4mm (afni documentation) and paper by Chen and Cox used 4mm too
# Erode or not erode: https://discuss.afni.nimh.nih.gov/t/erode-fs-ap-wm-nii-gz-from-suma-make-spec-fs/2854
