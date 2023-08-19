import os
import random

def count_bvh_files(directory):
    bvh_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.bvh'):
                bvh_files.append(file)

    return bvh_files

def assign_random_camera_numbers(bvh_files):
    return [random.randint(1, 3) for _ in range(len(bvh_files))]

def save_to_camera_txt(bvh_files, camera_numbers, filename):
    with open(filename, 'w') as file:
        for cam_num in camera_numbers:
            file.write(str(cam_num) + '\n')

if __name__ == "__main__":
    target_directory = r"C:\Users\cyh23\Desktop\论文复现\HD-GCN-main\data\he2023"
    bvh_files = count_bvh_files(target_directory)
    camera_numbers = assign_random_camera_numbers(bvh_files)
    save_to_camera_txt(bvh_files, camera_numbers, "camera.txt")
    print("camera.txt 文件已生成。")
