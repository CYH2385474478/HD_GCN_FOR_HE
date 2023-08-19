joints = [
    "Hips",
    "Spine",
    "Spine1",
    "Spine2",
    "Spine3",
    "Neck",
    "Neck1",
    "Head",
    "HeadEnd",
    "End Site1",  # End Site of the HeadEnd
    "RightShoulder",
    "RightArm",
    "RightForeArm",
    "RightHand",
    "RightHandThumb1",
    "End Site2",  # End Site of the RightHandThumb1
    "RightHandMiddle1",
    "End Site3",  # End Site of the RightHandMiddle1
    "LeftShoulder",
    "LeftArm",
    "LeftForeArm",
    "LeftHand",
    "LeftHandThumb1",
    "End Site4",  # End Site of the LeftHandThumb1
    "LeftHandMiddle1",
    "End Site5",  # End Site of the LeftHandMiddle1
    "RightUpLeg",
    "RightLeg",
    "RightFoot",
    "RightForeFoot",
    "RightToeBase",
    "RightToeBaseEnd",
    "End Site6",  # End Site of the RightToeBaseEnd
    "LeftUpLeg",
    "LeftLeg",
    "LeftFoot",
    "LeftForeFoot",
    "LeftToeBase",
    "LeftToeBaseEnd",
    "End Site7"  # End Site of the LeftToeBaseEnd
]

# Create a dictionary to map joint names to indices
joint_to_idx = {joint: idx+1 for idx, joint in enumerate(joints)}  # add 1 to each index to make them 1-based

# Define the pairs using the names of the joints
pairs = [
    ("Hips", "Spine"),
    ("Spine", "Spine1"),
    ("Spine1", "Spine2"),
    ("Spine2", "Spine3"),
    ("Spine3", "Neck"),
    ("Neck", "Neck1"),
    ("Neck1", "Head"),
    ("Head", "HeadEnd"),
    ("HeadEnd", "End Site1"),
    ("Spine3", "RightShoulder"),
    ("RightShoulder", "RightArm"),
    ("RightArm", "RightForeArm"),
    ("RightForeArm", "RightHand"),
    ("RightHand", "RightHandThumb1"),
    ("RightHandThumb1", "End Site2"),
    ("RightHand", "RightHandMiddle1"),
    ("RightHandMiddle1", "End Site3"),
    ("Spine3", "LeftShoulder"),
    ("LeftShoulder", "LeftArm"),
    ("LeftArm", "LeftForeArm"),
    ("LeftForeArm", "LeftHand"),
    ("LeftHand", "LeftHandThumb1"),
    ("LeftHandThumb1", "End Site4"),
    ("LeftHand", "LeftHandMiddle1"),
    ("LeftHandMiddle1", "End Site5"),
    ("Hips", "RightUpLeg"),
    ("RightUpLeg", "RightLeg"),
    ("RightLeg", "RightFoot"),
    ("RightFoot", "RightForeFoot"),
    ("RightForeFoot", "RightToeBase"),
    ("RightToeBase", "RightToeBaseEnd"),
    ("RightToeBaseEnd", "End Site6"),
    ("Hips", "LeftUpLeg"),
    ("LeftUpLeg", "LeftLeg"),
    ("LeftLeg", "LeftFoot"),
    ("LeftFoot", "LeftForeFoot"),
    ("LeftForeFoot", "LeftToeBase"),
    ("LeftToeBase", "LeftToeBaseEnd"),
    ("LeftToeBaseEnd", "End Site7")
]

# Convert the pairs to indices
pairs_idx = [(joint_to_idx[j1], joint_to_idx[j2]) for j1, j2 in pairs]

print(pairs_idx)
