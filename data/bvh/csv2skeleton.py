import pandas as pd
import numpy as np
import os
from tqdm import tqdm

def process_csv(file_path, skeleton_file_path, local_bodyID):
    # Read CSV file
    df = pd.read_csv(file_path)

    # Number of frames
    num_frames = len(df)

    # Open skeleton file for writing
    with open(skeleton_file_path, 'w') as file:
        # Write the total number of frames to the first line of the file
        file.write(f'{num_frames}\n')

        # For each frame, extract all joint positions and write them to the file
        for frame in range(num_frames):
            # Write the number of skeletons to the next line
            file.write('1\n')

            # Write the local_bodyID to the next line
            file.write(local_bodyID + ' ' +'1'+' 1'+' 1'+' 0'+' 0'+' 0'+' 0'+' 0'+' 0'+'\n')

            file.write('40\n')

            frame_data = df.iloc[frame]
            frame_dict = {}
            for joint in frame_data.keys():
                joint_parts = joint.split(':')
                if len(joint_parts) == 3:
                    prefix, joint_name, coordinate = joint_parts
                    if joint_name not in frame_dict:
                        frame_dict[joint_name] = {}
                    frame_dict[joint_name][coordinate] = frame_data[joint]

            # Write the values to the skeleton file
            for joint_name in frame_dict:
                values = []
                for index, coordinate in enumerate(sorted(frame_dict[joint_name].keys())):
                    if index % 3 == 0 and index != 0:
                        file.write(' '.join(map(str, values)) + ' 0 0 0 0 0 0 0 0 2\n')  # Add extra values and newline
                        values = []
                    values.append(frame_dict[joint_name][coordinate])

                file.write(' '.join(map(str, values)) + ' 0 0 0 0 0 0 0 0 2\n')

def process_directory(directory_path, body_id_file_path):
    # First, read the body_ids from the text file
    with open(body_id_file_path, 'r') as f:
        body_ids = f.read().splitlines()

    # Create an iterator for the body_ids
    body_id_iter = iter(body_ids)

    # Count the number of csv files
    num_csv_files = sum([file.endswith('.csv') for root, dirs, files in os.walk(directory_path) for file in files])

    with tqdm(total=num_csv_files, desc="Processing CSV files") as pbar:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.csv'):
                    file_path = os.path.join(root, file)
                    subdir_name = os.path.basename(root)
                    skeleton_file_name = subdir_name + '_' + os.path.splitext(file)[0] + '.skeleton'
                    skeleton_file_path = os.path.join(root, skeleton_file_name)
                    local_bodyID = next(body_id_iter)  # Get the next body_id
                    process_csv(file_path, skeleton_file_path, local_bodyID)
                    pbar.update()  # Update the progress bar

# Specify the root directory path
root_directory_path = r'C:\Users\cyh23\Desktop\论文复现\HD-GCN-main\data\he2023'  # Replace with your actual directory path

# Specify the body id file path
body_id_file_path = r'C:\Users\cyh23\Desktop\论文复现\HD-GCN-main\data\he2023\body_ids.txt'  # Replace with your actual body id file path

# Process all CSV files in the directory and its subdirectories
process_directory(root_directory_path, body_id_file_path)
