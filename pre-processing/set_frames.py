import pickle

# 替换为你实际的 pkl 文件路径
pkl_file_path = r"C:\Users\cyh23\Desktop\论文复现\HD-GCN-main\data\bvh\raw_data\raw_skes_data.pkl"

with open(pkl_file_path, 'rb') as f:
    data = pickle.load(f)

frames_cnt = [len(item['data']['BodyID']['Hips']['joints']) for item in data]

# 替换为你实际的输出 txt 文件路径
output_file_path = r"C:\Users\cyh23\Desktop\论文复现\HD-GCN-main\data\bvh\raw_data\frames_cnt.txt"

with open(output_file_path, 'w') as f:
    for count in frames_cnt:
        f.write(str(count) + '\n')

print("Frame counts have been written to", output_file_path)
