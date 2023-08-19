import os
import shutil

def move_skeleton_files(src_folder, dest_folder):
    # 确保目标文件夹存在
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # 遍历源文件夹及其子文件夹
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            # 检查文件扩展名是否为 .skeleton
            if file.endswith('.skeleton'):
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_folder, file)

                # 如果目标文件夹中已存在同名文件，则重命名
                count = 1
                while os.path.exists(dest_file_path):
                    name, ext = os.path.splitext(file)
                    dest_file_path = os.path.join(dest_folder, f"{name}_{count}{ext}")
                    count += 1

                # 移动文件
                shutil.move(src_file_path, dest_file_path)
                print(f"Moved {src_file_path} to {dest_file_path}")

# 源文件夹路径
src_folder = r'C:\Users\cyh23\Desktop\论文复现\HD-GCN-main\data\he2023'

# 目标文件夹路径
dest_folder = r'C:\Users\cyh23\Desktop\论文复现\HD-GCN-main\pre-processing\all_skl'

# 调用函数执行操作
move_skeleton_files(src_folder, dest_folder)
