from pathlib import Path
import shutil

# Define the project paths
project_path = Path("/nndb_teens/jure/MovieProject")
raw_data_path = project_path / "physio"
bids_data_path = project_path / "bids_data/sourcedata"

# Define exceptions for specific subjects and sessions where the first run was paused
paused_files_exceptions = {
    ('ID', 'IDInIn'): ["beforepause", "afterpause"],
    ('ID', 'IDInIn'): ["beforepause", "afterpause"]
}

# Define other exceptions if needed
# runs to skip
#runs_to_skip = {
#    ('12'): ["ced99085"]

#print("Starting the conversion of PULS log files to BIDS sourcedata format...")

# Iterate over each subject folder in raw_data
for subject_folder in sorted(raw_data_path.glob("Physio*")):
    print("Processing subject folder: ", subject_folder.name, flush=True)
    subject_id = subject_folder.name.split("o")[1]
    
    
    print(f"Subject ID: {subject_id}", flush=True)
    if subject_id in ['ID', 'ID']:
        continue

    # Gather and sort session folders by date (from session folder name)
    #session_folders = sorted(subject_folder.glob("sess-*"), key=lambda x: x.name[5:11])  # Sort by date part
    session_bids_id = "001"

    # Define the output path in BIDS format
    output_folder = bids_data_path / f"sub-{subject_id}" / f"ses-{session_bids_id}" / "func"
    output_folder.mkdir(parents=True, exist_ok=True)

    print(f"setting output directory as {output_folder}", flush=True)

    # Search for PULS.log files > 9.5 MB and > 1 MB for session 1 and 2 respectively
    if session_bids_id == "001": # session-1
        print(f"  Processing session folder: sess-{session_bids_id} and looking for puls file ", flush=True)
        puls_files = sorted([p for p in subject_folder.glob("*_PULS.log") if p.stat().st_size > 3 * 1024 * 1024])
        if len(puls_files) != 3:
            print(
                f"Warning for subject {subject_id}, "
                f"session {session_bids_id}: Found {len(puls_files)} "
                f"relevant PULS files. Expected 3 (3 BTF runs)")
    

    # Process each relevant PULS file
    run_id_btf = 1
    run_id_prf = 1
    run_id_tono = 1
    run_pause_i = 0

    for puls_file in puls_files:
        if any(substring in str(puls_file) for substring in ['c14b6aac-4b5b-4401-8c44-b4b2b756541d',
                                                                'e25f21eb-ed3f-462a-b184-2ef92e6e15cf']):
            continue

        # Extract unique identifier from PULS filename to find matching Info file
        unique_id = puls_file.stem.split("_")[3]

        # Search for the matching Info file in the same directory
        matching_info_file = next((f for f in subject_folder.glob(f"*{unique_id}*_Info.log")), None)

        if matching_info_file:

            # Check for paused run exceptions
            if (subject_id, subject_folder.name[5:]) in paused_files_exceptions and run_pause_i < 2:
                # Handle the paused run exception by adding `acq-beforepause` or `acq-afterpause`
                acq_labels = paused_files_exceptions[(subject_id, session_bids_id)]
                puls_bids_name = f"sub-{subject_id}_ses-{session_bids_id}_task-backtothefuture_acq-{acq_labels[run_pause_i]}_run-001_physioPULS.tsv"
                info_bids_name = f"sub-{subject_id}_ses-{session_bids_id}_task-backtothefuture_acq-{acq_labels[run_pause_i]}_run-001_physioInfo.tsv"
                run_pause_i += 1

                if run_pause_i == 2:
                    run_id_btf += 1

            # Define new filenames for BIDS format
            elif session_bids_id == "001":  # session-1
                puls_bids_name = f"sub-{subject_id}_ses-{session_bids_id}_run-{run_id_btf:03d}_task-backtothefuture_physioPULS.tsv"
                info_bids_name = f"sub-{subject_id}_ses-{session_bids_id}_run-{run_id_btf:03d}_task-backtothefuture_physioInfo.tsv"
                run_id_btf += 1
            
            # Copy and rename files to the BIDS directory
            shutil.copy(puls_file, output_folder / puls_bids_name)
            shutil.copy(matching_info_file, output_folder / info_bids_name)

            print(f"Copied {puls_file.name} to {puls_bids_name}")
            print(f"Copied {matching_info_file.name} to {info_bids_name}")

        else:
            print(
                f"Warning for subject {subject_id}, session {session_bids_id}: No matching Info file found for {puls_file.name}")
