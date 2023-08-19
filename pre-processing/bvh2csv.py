import os
import subprocess

# Set your directory path here
directory_path = r"E:\bvh_suoxiao"

for root, dirs, files in os.walk(directory_path):
    for filename in files:
        if filename.endswith(".bvh"):
            bvh_file_path = os.path.join(root, filename)
            # Run the bvh_converter module for each .bvh file
            subprocess.run(["python", "-m", "bvh_converter", bvh_file_path])
            print(f"Converted {bvh_file_path}")
