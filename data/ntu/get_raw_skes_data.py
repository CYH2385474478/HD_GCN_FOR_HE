import pandas as pd
import numpy as np
import os
import pickle

# 定义用于处理CSV文件并返回相应字典的函数
def process_csv(file_path):
    # 读取CSV文件
    df = pd.read_csv(file_path)

    # 计算数据行数
    num_frames = len(df)

    # 自动获取关节的数量
    num_joints = df.shape[1] // 3

    # 创建一个字典用于存储所有体位数据
    bodies_data = {}

    for i in range(num_joints):
        # 从CSV文件中提取每个关节的X、Y、Z坐标
        joint_data = df.values[:, i*3:i*3+3]
        bodies_data[f'joint_{i+1}'] = joint_data.tolist()  # 将numpy数组转化为列表以便于序列化

    # 构造返回的字典
    result = {
        'name': os.path.basename(file_path),
        'data': {
            'joints': bodies_data,  # 对所有关节的数据进行嵌套
            'colors': np.zeros((num_frames, num_joints, 2)).tolist(),  # 我们没有颜色信息，所以使用0填充
            'interval': list(range(num_frames)),  # 假设所有帧都是有效的
            'motion': None,  # 我们的CSV文件只有一个body
        },
        'num_frames': num_frames
    }
    return result

# 遍历所有目录和文件
root_dir = r'C:\Users\cyh23\Desktop\论文复现\HD-GCN-main\data\he2023'  # 这里替换为您的根目录
all_data = []  # 用于保存所有数据的列表
for category in os.listdir(root_dir):
    category_dir = os.path.join(root_dir, category)
    if os.path.isdir(category_dir):
        for file in os.listdir(category_dir):
            if file.endswith('.csv'):
                file_path = os.path.join(category_dir, file)
                data_dict = process_csv(file_path)
                all_data.append(data_dict)  # 添加数据字典到列表

# 将列表序列化为.pkl文件
with open(os.path.join(root_dir, 'all_data.pkl'), 'wb') as fw:
    pickle.dump(all_data, fw, pickle.HIGHEST_PROTOCOL)
