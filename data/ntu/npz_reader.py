
import numpy as np

def view_npz_file(npz_file_path, num_items=5):
    try:
        data = np.load(npz_file_path)
        print(f"Content of '{npz_file_path}':")
        print("=" * 30)
        for idx, (key, value) in enumerate(data.items()):
            print(f"Array name: {key}")
            print(value[:num_items])  # 使用切片来只打印前 num_items 个元素
            print("-" * 30)
            if idx >= num_items - 1:
                break
    except FileNotFoundError:
        print(f"Error: File '{npz_file_path}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    npz_file_path = input(r"C:\Users\cyh23\Desktop\论文复现\HD-GCN-main\data\ntu\NTU60_CS.npz")
    view_npz_file(npz_file_path)

