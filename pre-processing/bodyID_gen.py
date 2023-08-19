import os
import random

# Define the function to generate unique body IDs
def generate_body_id(existing_ids, length=17):
    # Generate a random body ID
    body_id = ''.join(random.choices('0123456789', k=length))

    # If the generated ID already exists, generate a new one
    while body_id in existing_ids:
        body_id = ''.join(random.choices('0123456789', k=length))

    # Add the new ID to the set of existing IDs
    existing_ids.add(body_id)

    return body_id, existing_ids

# Define the function to assign IDs to BVH files
def assign_ids_to_bvh_files(root_folder, output_file):
    existing_ids = set()

    # Open the output file
    with open(output_file, 'w') as f:
        # Walk through the root folder
        for dirpath, dirnames, filenames in os.walk(root_folder):
            # For each file in the current directory
            for filename in filenames:
                # If the file is a BVH file
                if filename.endswith('.bvh'):
                    # Generate a unique body ID
                    body_id, existing_ids = generate_body_id(existing_ids)

                    # Write the ID to the output file
                    f.write(body_id + '\n')

# Usage
root_folder = r'C:\Users\cyh23\Desktop\论文复现\HD-GCN-main\data\he2023'  # Replace with your root folder
output_file = 'body_ids.txt'  # Replace with your output file path
assign_ids_to_bvh_files(root_folder, output_file)
