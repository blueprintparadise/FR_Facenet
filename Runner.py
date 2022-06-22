import os
from deepface import DeepFace
cwd = os.getcwd()
DeepFace.stream(source=1,db_path = "deepface/images" ,model_name='Facenet',detector_backend = 'mtcnn',enable_face_analysis=False,time_threshold=1,frame_threshold=1)
