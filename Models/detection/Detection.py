import cv2
import cvlib as cv
from Models.detection.tracker import *
from image import Image
from threading import Thread

last_acc = None
last_id = None
boxes_ids = None
count = -1
id_accuracy_list = []


class Detection:
    tracker = EuclideanDistTracker()
    tackerList = []

    def detectFaces(self, image):
        global boxes_ids
        faces, confidences = cv.detect_face(image)
        for idx, face in enumerate(faces):
            x1, y1, x2, y2 = face
            self.tackerList.append([confidences[idx], x1, y1, x2, y2])
        boxes_ids = self.tracker.update(self.tackerList)

    def faceTracking(self, image, camNum):
        global count
        global last_acc
        global last_id
        global count
        global id_accuracy_list
        global boxes_ids
        self.tackerList = []
        self.detectFaces(image)
        print(id_accuracy_list)
        for box_id in boxes_ids:
            accuracy, start_x, start_y, end_x, end_y, id = box_id

            image = cv2.rectangle(image, (start_x, start_y), (end_x, end_y), (255, 0, 0), 1)

            # save image here
            if not id_accuracy_list:
                last_acc = accuracy
                last_id = id
                id_accuracy_list.append((id, accuracy))
                count += 1
                # t1 = Thread(target=Image, args=(image, start_y, end_y, start_x, end_x))
                # t1.start()
                Image(image, start_y, end_y, start_x, end_x, camNum, id)

            if (id == last_id) and (accuracy > last_acc):
                last_acc = accuracy
                last_id = id
                id_accuracy_list[count] = (id, accuracy)
                # t2 = Thread(target=Image, args=(image, start_y, end_y, start_x, end_x))
                # t2.start()
                #Image(image, start_y, end_y, start_x, end_x, camNum, id)
            elif id == last_id and accuracy < last_acc:
                continue
            elif id != last_id:
                #
                last_acc = accuracy
                last_id = id
                list = id_accuracy_list
                id_accuracy_list = []
                count -= 1
                id_accuracy_list.append((id, accuracy))
                count += 1
                Image(image, start_y, end_y, start_x, end_x, camNum, id)
                # threading.main_thread()

                # t3 = Thread(target=Image, args=(image, start_y, end_y, start_x, end_x))
                # t3.start()


        # print(self.id_accuracy_list)
        # save image here !
        return image
