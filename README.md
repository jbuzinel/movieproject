# movieproject
Scripts accompanying the NNDb-Teens dataset. Includes preprocessing and data quality checks.

The scripts were adapted from [https://github.com/levchenkoegor/movieproject2](https://github.com/levchenkoegor/movieproject2).

## Overview

This repository contains scripts for converting data to a BIDS-compliant format, preprocessing, analysing, and plotting data from the *Naturalistic Neuroimaging Database - Teens*. The accompanying paper, which describes the tasks, MRI protocols, quality control procedures, and more, is available [here](https://www.nature.com/articles/s41597-026-07676-4). The dataset itself is available on the [OpenNeuro repository](https://openneuro.org/datasets/ds006642/versions/1.1.1). Scripts used to analyse the task (backtothefuture) are provided in the relevant folder.

## Repository Structure

Here is a summary of the main files and folders:

| Script / Folder | Purpose |
|-----------------|---------|
| `conda-py-env.yml` | Conda environment specification file. |
| `01_convert_to_bids.sh` `add_intendedfor_field.py` `heuristic_sess01.py` `pulselog2sourcedata.py` | Convert all raw data into BIDS format. |
| `02_run_freesurfer.sh` | Run FreeSurfer processing on raw anatomical data. |
| `03_run_sswarper.sh` | Run `SSwarper` on raw anatomical data. |
| `04_run_suma.sh` | Run SUMA to convert FreeSurfer outputs into an AFNI-friendly format. |
| `05_plot_fd_alltasks.py` | Plot framewise displacement across all tasks (Figure 3 in the paper). |
| `backtothefuture` | Scripts used to analyse the task. |

## Requirements

To reproduce the outputs or run the scripts, the following dependencies are required:

- Python 3.12.8  
- Conda (or another environment manager) to create the `conda-py-env.yml` environment  
- FreeSurfer  
- AFNI  
- Bash environment for running the `.sh` scripts  
- Standard Python packages (NumPy, SciPy, pandas, matplotlib, etc.)

## Contributing

If you would like to contribute:

- Open an issue for bugs, questions, or feature requests  
- Fork the repository and submit a pull request  

## How to acknowledge

If you use this code or dataset in your work, please cite the associated paper:
