import numpy as np

# 假设你的数据保存在 'data.npz' 文件中，并且数据是字典形式保存的
data = np.load(r'C:\Users\cyh23\Desktop\论文复现\HD-GCN-main\data\ntu\NTU60_CS.npz')

# 打印数据的键
print(data.keys())

# 假设你想查看名为 'x_train' 的数据的形状
print(data['x_train'].shape)
