import os

# Specify the main directory path
main_dir_path = r'C:\Users\cyh23\Desktop\论文复现\HD-GCN-main\data\he2023'

# Create a list to store the subdirectories that contain .bvh files
bvh_dirs = []

# Go through each subdirectory in the main directory
for subdir in os.listdir(main_dir_path):
    # Create the full path of the sub-directory
    subdir_path = os.path.join(main_dir_path, subdir)

    # If this path is a directory and it contains .bvh files, add it to the list
    if os.path.isdir(subdir_path) and any(file.endswith('.bvh') for file in os.listdir(subdir_path)):
        bvh_dirs.append(subdir)

# Sort the list of subdirectories
bvh_dirs = sorted(bvh_dirs)

# Open the output file
with open('label.txt', 'w') as f:
    # Enumerate over each sub-directory in the sorted list of subdirectories
    for idx, subdir in enumerate(bvh_dirs, start=1):
        # Create the full path of the sub-directory
        subdir_path = os.path.join(main_dir_path, subdir)

        # Count the number of bvh files in this directory
        num_bvh_files = len([file for file in os.listdir(subdir_path) if file.endswith('.bvh')])

        # Write the directory number into the file as many times as there are bvh files
        for _ in range(num_bvh_files):
            f.write(f'{idx}\n')
