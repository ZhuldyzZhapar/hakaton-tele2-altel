from skimage import io
import dlib
import os
from scipy.spatial import distance


def get_description(path):
    shape_rec = dlib.shape_predictor('service/src/models/shape_predictor_68_face_landmarks.dat')
    face_rec = dlib.face_recognition_model_v1('service/src/models/dlib_face_recognition_resnet_model_v1.dat')
    detector = dlib.get_frontal_face_detector()
    image = io.imread(path)
    captured_rectangle = detector(image, 1)
    biggest_face = {}
    for k, d in enumerate(captured_rectangle):
        shape_res = shape_rec(image, d)

        square_rectangle = (d.right() - d.left()) * (d.bottom() - d.top())
        biggest_face[shape_res] = square_rectangle
    shape_result = max(biggest_face, key=biggest_face.get)
    face_descriptor = face_rec.compute_face_descriptor(image, shape_result)
    return face_descriptor


def face_verification():
    print(os.getcwd())
    face_id_path = 'service/src/images/img_card/'
    face_check_path = 'service/src/images/img_selfie/'

    face_id_to = os.listdir(face_id_path)
    face_id_to.sort(key=lambda x: os.path.getmtime(face_id_path + x))
    face_id = face_id_to[-1]
    face_check_to = os.listdir(face_check_path)
    face_check_to.sort(key=lambda x: os.path.getmtime(face_check_path + x))
    face_check = face_check_to[-1]

    id_description = get_description(face_id_path + face_id)
    check_description = get_description(face_check_path + face_check)
    comparison = distance.euclidean(id_description, check_description)
    return str(round(100 - comparison, 2)) + '%'
