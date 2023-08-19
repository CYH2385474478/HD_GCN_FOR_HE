import pandas as pd
import numpy as np
import os
import pickle
from tqdm import tqdm

# List of joints
joints = ['Hips', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftForeFoot', 'LeftToeBase', 'LeftToeBaseEnd', 'LeftToeBaseEndEnd',
          'RightUpLeg', 'RightLeg', 'RightFoot', 'RightForeFoot', 'RightToeBase', 'RightToeBaseEnd', 'RightToeBaseEndEnd',
          'Spine', 'Spine1', 'Spine2', 'Spine3', 'LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand', 'LeftHandMiddle1',
          'LeftHandMiddle1End', 'LeftHandThumb1', 'LeftHandThumb1End', 'RightShoulder', 'RightArm', 'RightForeArm',
          'RightHand', 'RightHandMiddle1', 'RightHandMiddle1End', 'RightHandThumb1', 'RightHandThumb1End', 'Neck', 'Neck1',
          'Head', 'HeadEnd', 'HeadEndEnd']

def process_csv(file_path):
    # Read CSV file
    df = pd.read_csv(file_path)

    # Number of frames
    num_frames = len(df)

    # Create a dictionary to store all body data
    bodies_data = {}

    # For each joint, extract X, Y, Z coordinates and convert to ntu format
    for frame in range(num_frames):
        for joint in joints:
            joint_cols = [col for col in df.columns if joint in col]
            joint_data = df.loc[frame, joint_cols].values
            joint_data = joint_data.reshape(-1, 3)
            if joint not in bodies_data:
                bodies_data[joint] = {
                    'joints': joint_data,
                    'colors': np.zeros((1, 2)),  # Add 2D color information
                    'interval': [frame]
                }
            else:
                bodies_data[joint]['joints'] = np.vstack((bodies_data[joint]['joints'], joint_data))
                bodies_data[joint]['colors'] = np.vstack((bodies_data[joint]['colors'], np.zeros((1, 2))))
                bodies_data[joint]['interval'].append(frame)

    # Construct the returning dictionary
    result = {
        'name': os.path.basename(file_path),
        'data': {'BodyID': bodies_data},  # Add body ID
        'num_frames': num_frames
    }

    return result

# Traverse all directories and files
root_dir = r'C:\Users\cyh23\Desktop\论文复现\HD-GCN-main\data\he2023'  # Replace with your root directory

all_data = []  # Store all data

file_list = []  # File list to process
for category in os.listdir(root_dir):
    category_dir = os.path.join(root_dir, category)
    if os.path.isdir(category_dir):
        for file in os.listdir(category_dir):
            if file.endswith('.csv'):
                file_path = os.path.join(category_dir, file)
                file_list.append(file_path)

# Process each file with a progress bar
for file_path in tqdm(file_list, desc="Processing files", unit="file"):
    data_dict = process_csv(file_path)
    all_data.append(data_dict)

save_dir = r'C:\Users\cyh23\Desktop\论文复现\HD-GCN-main\data\bvh'
# Serialize the dictionary into a .pkl file
with open(os.path.join(save_dir, 'raw_skes_data.pkl'), 'wb') as fw:
    pickle.dump(all_data, fw, pickle.HIGHEST_PROTOCOL)
