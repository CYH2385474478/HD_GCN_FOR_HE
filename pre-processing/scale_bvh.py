import bpy
import os

# Specify the top-level directory
dir_path = r"C:\Users\cyh23\Desktop\论文复现\HD-GCN-main\data\he2023"

# Specify the scale factor
scale_factor = 0.04  # change this to the scale factor you want

# Walk through the directory
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith(".bvh"):
            # Full path of the BVH file to import
            import_filepath = os.path.join(root, file)

            # Import the BVH file
            bpy.ops.import_anim.bvh(filepath=import_filepath)

            # Get the total number of frames
            frames = bpy.context.object.animation_data.action.fcurves[0].keyframe_points
            total_frames = int(frames[-1].co[0])  # the total number of frames is the x-coordinate of the last keyframe

            # Export the BVH file with the same total number of frames as the imported file
            bpy.ops.export_anim.bvh(filepath=import_filepath, global_scale=scale_factor, frame_start=1,
                                    frame_end=total_frames)

            # Delete the imported object to free up memory
            bpy.ops.object.delete()
