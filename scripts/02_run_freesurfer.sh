#!/bin/bash

# Setup freesurfer and directories
export FREESURFER_HOME=/software/freesurfer
source $FREESURFER_HOME/SetUpFreeSurfer.sh

export SUBJECTS_DIR=/nndb_teens/jure/MovieProject/bids_data/derivatives/freesurfer/
export data_folder=/nndb_teens/jure/MovieProject/bids_data

# Extract subject IDs dynamically from the bids_data folder
subjects="XXX" # This is a static list, but could be dynamically generated if needed

# $(ls -d $data_folder/sub-* | awk -F'/' '{print $NF}' | sed 's/sub-//') this could be used to dynamically get IDs

# Check if folder SUBJECTS_DIR already exists
if [ -d "$SUBJECTS_DIR" ]; then
echo "SUBJECTS_DIR exists..."
else
  echo "SUBJECTS_DIR doesn't exist. Creating one now..."
  mkdir -p "$SUBJECTS_DIR"
fi

# Run
for subj_id in $subjects; do

  input_path="$data_folder/sub-${subj_id}/ses-001/anat/sub-${subj_id}_ses-001_T1w.nii.gz"

  echo $(freesurfer --version)
  echo "$subj_id freesurfer processing..."

  recon-all \
    -i "$input_path" \
    -s sub-"$subj_id" \
    -all
done
