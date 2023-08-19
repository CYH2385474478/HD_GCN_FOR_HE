import os

def get_bvh_files_names(directory):
    bvh_files_names = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.bvh'):
                folder_name = os.path.basename(root)
                file_name = os.path.splitext(file)[0]
                full_name = folder_name + file_name
                bvh_files_names.append(full_name)

    return bvh_files_names

def save_to_skes_available_name_txt(bvh_files_names, filename):
    with open(filename, 'w') as file:
        for file_name in bvh_files_names:
            file.write(file_name + '\n')

if __name__ == "__main__":
    target_directory = r"C:\Users\cyh23\Desktop\论文复现\HD-GCN-main\data\he2023"
    bvh_files_names = get_bvh_files_names(target_directory)
    save_to_skes_available_name_txt(bvh_files_names, "skes_available_name.txt")
    print("skes_available_name.txt 文件已生成。")
