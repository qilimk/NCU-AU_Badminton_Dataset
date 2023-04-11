# NCU-AU_Badminton_Dataset

## Download and Install `ffmpeg`

Please choose [ffmpeg](https://ffmpeg.org/download.html) based on your OS and install it before running the scripts. 

## WorkDir structure

```bash
├── preprocess_video
│   ├── *_preprocess.mp4
├── 2022-09-07_19-54-42_dataset
│   ├── label
│   │   ├── set1.csv
├── results
├── action_labels.txt
├── read_human_labelsl.py
├── sort_results.sh
└── .gitignore
```

## Read the labels and sort the files into classified folders

1. Make sure to follow the folder [structure](#workdir-structure).

2. Download the annotation folder (e.g., `2022-09-07_19-54-42_dataset`) into this workspace.

3. Run the script `read_human_labels.py` to split the original files and rename the new clips. 

    ```python
    python read_human_labels.py --folder_name 2022-09-07_19-54-42_dataset
    ``` 
    The new clips would be named like `2022-09-07_19-02-20_dataset_set1_135_010522_010568_B_00.mp4` based on the labels. 
4. Move all the clips you get from last step into a new folder like `badminton_dataset_tw` and run the scipt `sort_results.sh` to relocate the clips into classified folders. 

    ```bash 
    bash sort_results.sh badminton_dataset_tw
    ```