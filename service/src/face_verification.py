print("start")
import face_recognition
import cv2
import numpy
import os
from skimage import io


def face_verification(): #face_id, face_check
    tolerance = 0.6
    MODEL = 'cnn'
    face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    face_id_path = 'service/src/images/img_card/'
    face_check_path = 'service/src/images/img_selfie/'
    crop_id_photo = 'service/src/images/id_photo_crop.jpg'

    face_id_to = os.listdir(face_id_path)
    face_id_to.sort(key=lambda x: os.path.getmtime(face_id_path + x))
    face_id = face_id_to[-1]
    print(face_id)
    face_check_to = os.listdir(face_check_path)
    face_check_to.sort(key=lambda x: os.path.getmtime(face_check_path + x))
    face_check = face_check_to[-1]
    img_id = io.imread(face_id_path + face_id)
    faces = face_cascade_db.detectMultiScale(img_id, 1.1, 19)
    img_id_gray = cv2.cvtColor(img_id, cv2.COLOR_BGRA2GRAY)
    for (x, y, w, h) in faces:
        left = 10
        right = 10
        top = 10
        bottom = 10

        cv2.rectangle(img_id, (x, y), (x + w, y + h), (0, 255, 0), 2)
        img_id = img_id_gray[y - top:y + h + bottom, x - left:x + w + right]
    cv2.imwrite(crop_id_photo, img_id)

    img_id_crop = face_recognition.load_image_file(face_check_path + face_check)
    encoded_face_id = face_recognition.face_encodings(img_id_crop)[0]
    # ---------------------
    img_check = face_recognition.load_image_file(face_check_path + face_check)

    face_location = face_recognition. face_locations(img_check, model=MODEL)
    # face_location = [(371, 646, 878, 139)]
    encoded_face_check = face_recognition.face_encodings(img_check, face_location)
    result = face_recognition.compare_faces(encoded_face_id, encoded_face_check, tolerance)

    return result[0]













