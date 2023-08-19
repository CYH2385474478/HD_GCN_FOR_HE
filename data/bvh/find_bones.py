def get_bone_pairs(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    bone_pairs = []
    stack = []
    inside_end_site = False
    for line in lines:
        # remove leading and trailing whitespace
        line = line.strip()

        if "ROOT" in line or "JOINT" in line:
            # a new bone starts
            bone_name = line.split()[-1]
            if stack:
                # the previous bone is the parent of the current one
                bone_pairs.append((stack[-1], bone_name))
            stack.append(bone_name)
            inside_end_site = False
        elif "End Site" in line:
            # the "End Site" is a child of the current bone
            end_site_name = stack[-1] + "_End"
            bone_pairs.append((stack[-1], end_site_name))
            stack.append(end_site_name)
            inside_end_site = True
        elif "}" in line:
            # a bone ends
            if not inside_end_site:
                stack.pop()
            else:
                stack.pop()
                inside_end_site = False

    return bone_pairs

# usage:
bone_pairs = get_bone_pairs(r'C:\Users\cyh23\Desktop\论文复现\HD-GCN-main\data\he2023\comfortCrying_comfort\haolin&yihan_28_06_01.bvh')
print(bone_pairs)
