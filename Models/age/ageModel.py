import cv2
import numpy as np
import os


class AgeModel:

    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.age_model = cv2.dnn.readNetFromCaffe(
            os.path.join(current_dir, "model/age.prototxt"),
            os.path.join(current_dir, "model/dex_chalearn_iccv2015.caffemodel"))

    def startModel(self, img_blob_face):
        self.age_model.setInput(img_blob_face)
        age_dist = self.age_model.forward()[0]
        output_indexes = np.array([i for i in range(0, 101)])
        apparent_predictions = round(np.sum(age_dist * output_indexes))
        return apparent_predictions
