#!/bin/bash


# Setup directories
export PATH=/software/afni:$PATH
export PATH=/software/freesurfer/bin:$PATH
export FREESURFER_HOME=/software/freesurfer
source $FREESURFER_HOME/SetUpFreeSurfer.sh
#source $FREESURFER_HOME/SetUpFreeSurfer.sh

export data_folder=/nndb_teens/jure/MovieProject/bids_data

# Extract subject IDs dynamically from the bids_data folder
subjects="XXX" # This is a static list, but could be dynamically generated if needed
# subjects=$(ls -d $data_folder/derivatives/freesurfer/sub-* | awk -F'/' '{print $NF}' | sed 's/sub-//')

for subj_id in $subjects; do

    # Warp away
    OMP_NUM_THREADS=16 @SUMA_Make_Spec_FS \
      -fspath "$data_folder/derivatives/freesurfer/sub-${subj_id}" \
      -NIFTI \
      -sid sub-"${subj_id}"

    # Compress results
    gzip "${data_folder}"/derivatives/freesurfer/sub-"${subj_id}"/SUMA/*nii
    gzip "${data_folder}"/derivatives/freesurfer/sub-"${subj_id}"/SUMA/*gii

done
