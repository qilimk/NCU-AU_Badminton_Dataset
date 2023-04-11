import pandas as pd
import subprocess
import numpy as np
import argparse
import os

def read_csv(file_name):
    """
    Reads a csv file and returns a dataframe
    """
    return pd.read_csv(file_name)

def isNaN(string):
    return string != string

def main():
    """
    Main function
    """
    # Create the parser
    parser = argparse.ArgumentParser()
    # Add an argument
    parser.add_argument('--folder_name', type=str, default='2022-08-30_18-18-31_dataset')
    parser.add_argument('--anno_file', type=str, default='action_labels.txt')
    # Parse the argument
    args = parser.parse_args()
    
    preprocess_date = args.folder_name[:19]
    results_path = f'results/{preprocess_date}_results'

    if not os.path.exists(results_path):
        os.makedirs(results_path)

    annotations_list = ['set1']
    index = 0
    actions_dict = {}
    # cap = cv2.VideoCapture("/home/ubuntu/qf_ms_2020_data/_8Vy3dlHg2w_00106.mp4")
    with open(args.anno_file) as f:
        for l in f:
            actions_dict[l.rstrip()] = index
            index += 1

    for anno in annotations_list:
        df = read_csv(f'{args.folder_name}/label/{anno}.csv')
        for idx, start_frame_idx, end_frame_idx, label, player in zip(df.index.to_list(), df['frame_num'].to_list(), df['end_frame_num'].to_list(), df['type'].to_list() ,df['player'].to_list()):
            start_frame_idx = int(start_frame_idx)
            end_frame_idx =int(end_frame_idx)
            idx = int(idx)

            if isNaN(label):
                save_name = f"{results_path}/{args.folder_name}_{anno}_{idx:03d}_{start_frame_idx:06d}_{end_frame_idx:06d}_{player}_NO_Label.mp4"
            else:
                save_name = f"{results_path}/{args.folder_name}_{anno}_{idx:03d}_{start_frame_idx:06d}_{end_frame_idx:06d}_{player}_{actions_dict[label]:02d}.mp4"
            print(save_name)
            # cap.set(1, start_frame_idx)
            # ret, frame = cap.read()
            # cv2.imwrite(save_name, frame)
            #  ffmpeg -ss 1 -i _8Vy3dlHg2w_00106.mp4 -c:v libx264 -c:a aac -frames:v 35 out.mp4
            subprocess.call(f'ffmpeg -ss {start_frame_idx/30} -i preprocess_video/{preprocess_date}_preprocess.mp4 -c:v libx264 -c:a aac -frames:v {end_frame_idx -start_frame_idx } {save_name}'
                        , shell=True)

if __name__ == '__main__':
    main()