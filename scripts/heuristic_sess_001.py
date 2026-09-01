from __future__ import annotations

import logging
from typing import Optional

from heudiconv.utils import SeqInfo

lgr = logging.getLogger("heudiconv")


def create_key(
    template: Optional[str],
    outtype: tuple[str, ...] = ("nii.gz",),
    annotation_classes: None = None,
) -> tuple[str, tuple[str, ...], None]:
    if template is None or not template:
        raise ValueError("Template must be a valid format string")
    return (template, outtype, annotation_classes)


def infotodict(
    seqinfo: list[SeqInfo],
) -> dict[tuple[str, tuple[str, ...], None], list[str]]:
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """

    t1w = create_key('sub-{subject}/{session}/anat/sub-{subject}_{session}_T1w')

    # Run 1
    func_bttf_r1 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_run-001_bold')
    func_bttf_sbref_r1 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_run-001_sbref')
    fmap_bttf_phaserev_r1 = create_key('sub-{subject}/{session}/fmap/sub-{subject}_{session}_acq-func_dir-PA_run-001_epi')

    # Run 2
    func_bttf_r2 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_run-002_bold')
    func_bttf_sbref_r2 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_run-002_sbref')
    fmap_bttf_phaserev_r2 = create_key('sub-{subject}/{session}/fmap/sub-{subject}_{session}_acq-func_dir-PA_run-002_epi')

    # Run 3
    func_bttf_r3 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_run-003_bold')
    func_bttf_sbref_r3 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_run-003_sbref')
    fmap_bttf_phaserev_r3 = create_key('sub-{subject}/{session}/fmap/sub-{subject}_{session}_acq-func_dir-PA_run-003_epi')

    # In case of movie pausing (sub 36)
    func_bttf_r1_before_pause = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-beforepause_run-001_bold')
    func_bttf_sbref_r1_before_pause = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-beforepause_run-001_sbref')
    func_bttf_r1_after_pause = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-afterpause_run-001_bold')
    func_bttf_sbref_r1_after_pause = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-afterpause_run-001_sbref')
    func_bttf_r1_remove = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-remove_run-001_bold')
    func_bttf_r2_before_pause = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-beforepause_run-002_bold')
    func_bttf_sbref_r2_before_pause = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-beforepause_run-002_sbref')
    func_bttf_r2_after_pause = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-afterpause_run-002_bold')
    func_bttf_sbref_r2_after_pause = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-afterpause_run-002_sbref')
    func_bttf_r2_part1 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-part1_run-002_bold')
    func_bttf_sbref_r2_part1 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-part1_run-002_sbref')
    func_bttf_r2_part2 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-part2_run-002_bold')
    func_bttf_sbref_r2_part2 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-part2_run-002_sbref')
    func_bttf_r2_part3 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-part3_run-002_bold')
    func_bttf_sbref_r2_part3 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-part3_run-002_sbref')
    func_bttf_r2_part4 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-part4_run-002_bold')
    func_bttf_sbref_r2_part4 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-part4_run-002_sbref')
    func_bttf_r3_remove = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-remove_run-003_bold')
    func_bttf_r3_remove1 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-remove1_run-003_bold')
    func_bttf_sbref_r3_remove = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-remove_run-003_sbref')
    func_bttf_sbref_r3_remove1 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-remove1_run-003_sbref')
    func_bttf_r3_before_pause = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-beforepause_run-003_bold')
    func_bttf_sbref_r3_before_pause = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-beforepause_run-003_sbref')
    func_bttf_r3_after_pause = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-afterpause_run-003_bold')
    func_bttf_sbref_r3_after_pause = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-backtothefuture_acq-afterpause_run-003_sbref')
    


    info = {t1w: [], func_bttf_r1: [], func_bttf_sbref_r1: [], fmap_bttf_phaserev_r1: [], #run 1
                     func_bttf_r2: [], func_bttf_sbref_r2: [], fmap_bttf_phaserev_r2: [], #run 2
                     func_bttf_r3: [], func_bttf_sbref_r3: [], fmap_bttf_phaserev_r3: [], #run 3
                     func_bttf_r1_before_pause: [], func_bttf_sbref_r1_before_pause: [], func_bttf_r1_after_pause: [], func_bttf_sbref_r1_after_pause: [], # run 1 with one pause
                     func_bttf_r2_before_pause: [], func_bttf_sbref_r2_before_pause: [], func_bttf_r2_after_pause: [], func_bttf_sbref_r2_after_pause: [], # run 2 with one pause
                     func_bttf_r3_before_pause: [], func_bttf_sbref_r3_before_pause: [], func_bttf_r3_after_pause: [], func_bttf_sbref_r3_after_pause: [], # run 3 with one pause
                     func_bttf_r2_part1: [], func_bttf_sbref_r2_part1: [], func_bttf_r2_part2: [], func_bttf_sbref_r2_part2: [],
                     func_bttf_r2_part3: [], func_bttf_sbref_r2_part3: [], func_bttf_r2_part4: [], func_bttf_sbref_r2_part4: [], # run 2 with many pauses
                     func_bttf_r1_remove: [], func_bttf_sbref_r3_remove: [], func_bttf_r3_remove: [], func_bttf_r3_remove1: [], func_bttf_sbref_r3_remove1: []} # run 1 and 3 to be removed later


    # Tricks to include correct SBRef images in scenarios when the protocol was stopped and started again.
    # It creates several SBRef files which can be distinguished only by 'time' variable.
    # However, the loop below iterates over seqinfo in ascending order which means SBRef before multi-band movie task.
    # To address this issue and store only correct SBRefs and runs, the dict 'seqinfo' sorted in descending order and
    # correct SBRef image is included by 'time' variable

    seqinfo_descending = sorted(seqinfo, key=lambda item: float(item.time) if item.time is not None else float('-inf'), reverse=True)
    time_btf_run1, time_btf_run2, time_btf_run3 = 10000000000000000, 10000000000000000, 10000000000000000
    time_btf_run1_before_pause, time_btf_run1_after_pause = 10000000000000000, 10000000000000000
    time_btf_run2_before_pause, time_btf_run2_after_pause = 10000000000000000, 10000000000000000
    time_btf_run3_before_pause, time_btf_run3_after_pause = 10000000000000000, 10000000000000000
    time_btf_run2_part1, time_btf_run2_part2, time_btf_run2_part3, time_btf_run2_part4 = 10000000000000000, 10000000000000000, 10000000000000000, 10000000000000000
    time_btf_run3_remove, time_btf_run3_remove1 = 10000000000000000, 10000000000000000

    # Check if the subject has not ideal scenario (more or less nii files it is supposed to be)
    if len(seqinfo_descending) > 15:
        print(f'There are more files that it is supposed to be ({len(seqinfo)}), consider checking the output...')
    elif len(seqinfo_descending) < 15:
        print(f'There are less files that it is supposed to be ({len(seqinfo)}), consider checking the output...')

    for s in seqinfo_descending:
        """
        The namedtuple `s` contains the following fields:

        * total_files_till_now
        * example_dcm_file
        * series_id
        * dcm_dir_name
        * unspecified2
        * unspecified3
        * dim1
        * dim2
        * dim3
        * dim4
        * TR
        * TE
        * protocol_name
        * is_motion_corrected
        * is_derived
        * patient_id
        * study_description
        * referring_physician_name
        * series_description
        * image_type
        """

        # Handling exceptions
        if s.patient_id == 'P001669': #sub-04 (run 2 paused 3 times)
            if ('task-backtothefuture_run-2' in s.series_description) and (s.dim4 == 58): #before first pause in run 2
                info[func_bttf_r2_part1].append(s.series_id)
                time_btf_run2_part1 = float(s.time)
            if ('task-backtothefuture_run-2_SBRef' in s.series_description) and (time_btf_run2_part1 - float(s.time)) < 60:
                info[func_bttf_sbref_r2_part1].append(s.series_id)

            if ('task-backtothefuture_run-2' in s.series_description) and (s.dim4 == 395): #before second pause in run 2
                info[func_bttf_r2_part2].append(s.series_id)
                time_btf_run2_part2 = float(s.time)
            if ('task-backtothefuture_run-2_SBRef' in s.series_description) and (time_btf_run2_part2 - float(s.time)) < 60:
                info[func_bttf_sbref_r2_part2].append(s.series_id)

            if ('task-backtothefuture_run-2' in s.series_description) and (s.dim4 == 667): #before third pause in run 2
                info[func_bttf_r2_part3].append(s.series_id)
                time_btf_run2_part3 = float(s.time)
            if ('task-backtothefuture_run-2_SBRef' in s.series_description) and (time_btf_run2_part3 - float(s.time)) < 60:
                info[func_bttf_sbref_r2_part3].append(s.series_id)

            if ('task-backtothefuture_run-2' in s.series_description) and (s.dim4 == 490): #after third pause in run 2
                info[func_bttf_r2_part4].append(s.series_id)
                time_btf_run2_part4 = float(s.time)
            if ('task-backtothefuture_run-2_SBRef' in s.series_description) and (time_btf_run2_part4 - float(s.time)) < 60:
                info[func_bttf_sbref_r2_part4].append(s.series_id)
            
            if ('task-backtothefuture_run-3' in s.series_description) and (s.dim4 == 1577): #wrong number of TRs in run 3
                info[func_bttf_r3].append(s.series_id)
                time_btf_run3 = float(s.time)

        if s.patient_id == 'P001891': # sub-07 (pause in run 1, pause in run 2)
            if ('task-backtothefuture_run-1' in s.series_description) and (s.dim4 == 1096): #pause in run 1
                info[func_bttf_r1_before_pause].append(s.series_id)
                time_btf_run1_before_pause = float(s.time)
            if ('task-backtothefuture_run-1_SBRef' in s.series_description) and (time_btf_run1_before_pause - float(s.time)) < 60:
                info[func_bttf_sbref_r1_before_pause].append(s.series_id)

            if ('task-backtothefuture_run-1' in s.series_description) and (s.dim4 == 264):
                info[func_bttf_r1_after_pause].append(s.series_id)
                time_btf_run1_after_pause = float(s.time)
            if ('task-backtothefuture_run-1_SBRef' in s.series_description) and (time_btf_run1_after_pause - float(s.time)) < 60:
                info[func_bttf_sbref_r1_after_pause].append(s.series_id)

            if ('task-backtothefuture_run-2' in s.series_description) and (s.dim4 == 866): #pause in run 2
                info[func_bttf_r2_part1].append(s.series_id)
                time_btf_run2_part1 = float(s.time)
            if ('task-backtothefuture_run-2_SBRef' in s.series_description) and (time_btf_run2_part1 - float(s.time)) < 60:
                info[func_bttf_sbref_r2_part1].append(s.series_id)

            if ('task-backtothefuture_run-2' in s.series_description) and (s.dim4 == 640):
                info[func_bttf_r2_part2].append(s.series_id)
                time_btf_run2_part2 = float(s.time)
            if ('task-backtothefuture_run-2_SBRef' in s.series_description) and (time_btf_run2_part2 - float(s.time)) < 60:
                info[func_bttf_sbref_r2_part2].append(s.series_id)

            if ('task-backtothefuture_run-2' in s.series_description) and (s.dim4 == 46):
                info[func_bttf_r2_part3].append(s.series_id)
                time_btf_run2_part3 = float(s.time)
            if ('task-backtothefuture_run-2_SBRef' in s.series_description) and (time_btf_run2_part3 - float(s.time)) < 60:
                info[func_bttf_sbref_r2_part3].append(s.series_id)
        
        if s.patient_id == 'P001964': # sub-240129EH (pause in run 1, pause in run 2, extra stuff in run 3, P001964)
            print("Found sub-240129EH")

            if ('task-backtothefuture_run-1' in s.series_description) and (s.dim4 == 210): #pause in run 1
                info[func_bttf_r1_before_pause].append(s.series_id)
                time_btf_run1_before_pause = float(s.time)
            if ('task-backtothefuture_run-1_SBRef' in s.series_description) and (time_btf_run1_before_pause - float(s.time)) < 60:
                info[func_bttf_sbref_r1_before_pause].append(s.series_id)

            if ('task-backtothefuture_run-1' in s.series_description) and (s.dim4 == 1163):
                info[func_bttf_r1_after_pause].append(s.series_id)
                time_btf_run1_after_pause = float(s.time)
            if ('task-backtothefuture_run-1_SBRef' in s.series_description) and (time_btf_run1_after_pause - float(s.time)) < 60:
                info[func_bttf_sbref_r1_after_pause].append(s.series_id)

            if ('task-backtothefuture_run-2' in s.series_description) and (s.dim4 == 1097):
                info[func_bttf_r2_before_pause].append(s.series_id)
                time_btf_run2_before_pause = float(s.time)
            if ('task-backtothefuture_run-2_SBRef' in s.series_description) and (time_btf_run2_before_pause - float(s.time)) < 60:
                info[func_bttf_sbref_r2_before_pause].append(s.series_id)

            if ('task-backtothefuture_run-2' in s.series_description) and (s.dim4 == 439):
                info[func_bttf_r2_after_pause].append(s.series_id)
                time_btf_run2_after_pause = float(s.time)
            if ('task-backtothefuture_run-2_SBRef' in s.series_description) and (time_btf_run2_after_pause - float(s.time)) < 60:
                info[func_bttf_sbref_r2_after_pause].append(s.series_id)

            if ('task-backtothefuture_run-3' in s.series_description) and (s.dim4 == 50): #some odd runs even thought there is a full one
                info[func_bttf_r3_remove].append(s.series_id)
                time_btf_run3_remove = float(s.time)
            if ('task-backtothefuture_run-3_SBRef' in s.series_description) and (time_btf_run3_remove - float(s.time)) < 60:
                info[func_bttf_sbref_r3_remove].append(s.series_id)

            if ('task-backtothefuture_run-3' in s.series_description) and (s.dim4 == 74):
                info[func_bttf_r3_remove1].append(s.series_id)
                time_btf_run3_remove1 = float(s.time)
            if ('task-backtothefuture_run-3_SBRef' in s.series_description) and (time_btf_run3_remove1 - float(s.time)) < 60:
                info[func_bttf_sbref_r3_remove1].append(s.series_id)
                
            if ('task-backtothefuture_run-3' in s.series_description) and (s.dim4 == 1608):
                info[func_bttf_r3].append(s.series_id)
                time_btf_run3 = float(s.time)
            if ('task-backtothefuture_run-3_SBRef' in s.series_description) and (time_btf_run3 - float(s.time)) < 60:
                info[func_bttf_sbref_r3].append(s.series_id)

        
        if s.patient_id == 'P002143': #sub-14 (incomplete run 1)
            if ('task-backtothefuture_run-1' in s.series_description) and (s.dim4 == 730):
                info[func_bttf_r1].append(s.series_id)
                time_btf_run1 = float(s.time)

        if s.patient_id == 'P002158': # sub-20 (restarted run 1, paused in run 2)
            if ('task-backtothefuture_run-1' in s.series_description) and (s.dim4 == 68): #restarting run 1
                info[func_bttf_r1_remove].append(s.series_id)
                time_btf_run1_remove = float(s.time)

            if ('task-backtothefuture_run-2' in s.series_description) and (s.dim4 == 14): #run 2 something funny with the 14
                info[func_bttf_r2_part1].append(s.series_id)
                time_btf_run2_part1 = float(s.time)
            if ('task-backtothefuture_run-2' in s.series_description) and (s.dim4 == 845): #pause in run 2
                info[func_bttf_r2_part2].append(s.series_id)
                time_btf_run2_part2 = float(s.time)
            if ('task-backtothefuture_run-2_SBRef' in s.series_description) and (time_btf_run2_part2 - float(s.time)) < 60:
                info[func_bttf_sbref_r2_part2].append(s.series_id)
            if ('task-backtothefuture_run-2' in s.series_description) and (s.dim4 == 676):
                info[func_bttf_r2_part3].append(s.series_id)
                time_btf_run2_part3 = float(s.time)
            if ('task-backtothefuture_run-2_SBRef' in s.series_description) and (time_btf_run2_part3 - float(s.time)) < 60:
                info[func_bttf_sbref_r2_part3].append(s.series_id)

        if s.patient_id == 'P002182': # sub-22 (wrong cut of movie files)
            if ('task-backtothefuture_run-1' in s.series_description) and (s.dim4 == 1256):
                info[func_bttf_r1].append(s.series_id)
                time_btf_run1 = float(s.time)

        if s.patient_id == 'P002281': # sub-25 (wrong cut of movie files)
            if ('task-backtothefuture_run-2' in s.series_description) and (s.dim4 == 1504):
                info[func_bttf_r2].append(s.series_id)
                time_btf_run2 = float(s.time)

        if s.patient_id == 'P002409': # sub-29 (pause in second run, also incomplete, only keeping the first chunk of run 2)
            if ('task-backtothefuture_run-2' in s.series_description) and (s.dim4 == 766):
                info[func_bttf_r2].append(s.series_id)
                time_btf_run2 = float(s.time)

        if s.patient_id == 'P002460': # sub-32
            if ('task-backtothefuture_run-1' in s.series_description) and (s.dim4 == 308):
                info[func_bttf_r1].append(s.series_id)
                time_btf_run1 = float(s.time)

        if s.patient_id == 'P002473': # sub-33
            if ('task-backtothefuture_run-1' in s.series_description) and (s.dim4 == 1022):
                info[func_bttf_r1].append(s.series_id)
                time_btf_run1 = float(s.time)

        if s.patient_id == 'P003012': # sub-38
            if ('task-backtothefuture_run-2' in s.series_description) and (s.dim4 == 635): # pause in run 2
                info[func_bttf_r2_before_pause].append(s.series_id)
                time_btf_run2_before_pause = float(s.time)
            if ('task-backtothefuture_run-2_SBRef' in s.series_description) and (time_btf_run2_before_pause - float(s.time)) < 60:
                info[func_bttf_sbref_r2_before_pause].append(s.series_id)

            if ('task-backtothefuture_run-2' in s.series_description) and (s.dim4 == 906):
                info[func_bttf_r2_after_pause].append(s.series_id)
                time_btf_run2_after_pause = float(s.time)
            if ('task-backtothefuture_run-2_SBRef' in s.series_description) and (time_btf_run2_after_pause - float(s.time)) < 60:
                info[func_bttf_sbref_r2_after_pause].append(s.series_id)

        if s.patient_id == 'P003024': # sub-40
            if('task-backtothefuture_run-3' in s.series_description) and (s.dim4 == 1490): # pause in run 3
                info[func_bttf_r3_before_pause].append(s.series_id)
                time_btf_run3_before_pause = float(s.time)
            if ('task-backtothefuture_run-3_SBRef' in s.series_description) and (time_btf_run3_before_pause - float(s.time)) < 60:
                info[func_bttf_sbref_r3_before_pause].append(s.series_id)

            if ('task-backtothefuture_run-3' in s.series_description) and (s.dim4 == 135):
                info[func_bttf_r3_after_pause].append(s.series_id)
                time_btf_run3_after_pause = float(s.time)
            if ('task-backtothefuture_run-3_SBRef' in s.series_description) and (time_btf_run3_after_pause - float(s.time)) < 60:
                info[func_bttf_sbref_r3_after_pause].append(s.series_id)
        



        # anat
        if ('MPRAGE-GRAPPA2-1x1x1-208sl-100pcFOV' in s.series_description) and (s.dim3 == 208):
            info[t1w].append(s.series_id)
        # back to the future
        if ('task-backtothefuture_run-1' in s.series_description) and (s.dim4 == 1360):
            info[func_bttf_r1].append(s.series_id)
            time_btf_run1 = float(s.time)
        if ('task-backtothefuture_run-1_SBRef' in s.series_description) and (time_btf_run1 - float(s.time)) < 60:
            info[func_bttf_sbref_r1].append(s.series_id)
        if ('task-backtothefuture_run-1_PErev' == s.series_description):
            info[fmap_bttf_phaserev_r1].append(s.series_id)

        if ('task-backtothefuture_run-2' in s.series_description) and (s.dim4 == 1522):
            info[func_bttf_r2].append(s.series_id)
            time_btf_run2 = float(s.time)
        if ('task-backtothefuture_run-2_SBRef' in s.series_description) and (time_btf_run2 - float(s.time)) < 60:
            info[func_bttf_sbref_r2].append(s.series_id)
        if ('task-backtothefuture_run-2_PErev' ==  s.series_description):
            info[fmap_bttf_phaserev_r2].append(s.series_id)

        if ('task-backtothefuture_run-3' in s.series_description) and (s.dim4 == 1608):
            info[func_bttf_r3].append(s.series_id)
            time_btf_run3 = float(s.time)
        if ('task-backtothefuture_run-3_SBRef' in s.series_description) and (time_btf_run3 - float(s.time)) < 60:
            info[func_bttf_sbref_r3].append(s.series_id)
        if ('task-backtothefuture_run-3_PErev' == s.series_description):
            info[fmap_bttf_phaserev_r3].append(s.series_id)
    return info
    
