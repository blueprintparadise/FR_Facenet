import os

import DeepFace
cwd = os.getcwd()
DeepFace.stream(source=1,db_path = "images" ,model_name='Facenet',detector_backend = 'mtcnn',enable_face_analysis=False,time_threshold=1,frame_threshold=1)
