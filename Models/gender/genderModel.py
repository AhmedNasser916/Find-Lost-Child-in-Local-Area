import cv2
import numpy as np
import os


class GenderModel:

    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.gender_model = cv2.dnn.readNetFromCaffe(
            os.path.join(current_dir, "model/gender.prototxt"),
            os.path.join(current_dir, "model/gender.caffemodel"))

    def startModel(self, img_blob_face):
        self.gender_model.setInput(img_blob_face)
        gender_class = self.gender_model.forward()[0]
        return 'female' if np.argmax(gender_class) == 0 else 'male'
