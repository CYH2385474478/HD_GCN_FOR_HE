put all bvh files in he2023

RUN scale_bvh.py in blender
RUN bvh2csv.py
RUN bodyID_gen.py
RUN csv2skeleton.py
RUN camera_gen.py
RUN label_gen.py
RUN performer_gen.py
RUN skes_available_name_gen.py
RUN move_skl.py
RUN csv_get_raw_skes_data.py
RUN csv_get_raw_denoised_data.py
RUN csv_seq_transformation.py,change line 150  labels_vector = np.zeros((num_skes, 10)) （10 is the number of actions）
change joint_com_2.yaml line 31 as csv_seq_transformation