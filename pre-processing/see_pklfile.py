
import pickle


def peek_at_pickle_file(file_path, num_items=1):
    """
    Peek at the first few items in a pickle file.

    Parameters:
    file_path (str): Path to the pickle file.
    num_items (int): Number of items to peek at.
    """
    items = []
    with open(file_path, 'rb') as f:
        for _ in range(num_items):
            try:
                items.append(pickle.load(f))
            except EOFError:
                break
    return items

# Use the function to peek at the pickle file
items = peek_at_pickle_file(r'C:\Users\cyh23\Desktop\论文复现\HD-GCN-main\data\bvh\raw_data\raw_skes_data.pkl', num_items=5)
for item in items:
    print(item)
