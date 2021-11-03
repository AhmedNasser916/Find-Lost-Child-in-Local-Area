import cv2
from Models.gender.genderModel import GenderModel
from Models.age.ageModel import AgeModel
from datetime import datetime
import network.network as nt


class Image:
    def __init__(self, frame, start_y, end_y, start_x, end_x, camNum, id):
        self.frame = frame
        self.startY = start_y
        self.endY = end_y
        self.startX = start_x
        self.endX = end_x
        self.camNum = camNum
        self.id = id
        self.faceCropped = None
        self.faceGender = None
        self.faceAge = None
        self.path = None
        self.croppedFace()

        self.detectGender()

        self.detectAge()
        self.saveImage()
        self.sendImage()

    def croppedFace(self):
        self.faceCropped = self.frame[self.startY:self.endY, self.startX:self.endX]
        self.faceCropped = cv2.resize((cv2.cvtColor(self.faceCropped, cv2.COLOR_BGR2RGB)), (224, 224), 3)

    def detectGender(self):
        img_blob = cv2.dnn.blobFromImage(self.faceCropped)
        gm = GenderModel()
        self.faceGender = gm.startModel(img_blob)
        # return self.faceGender
        print(self.faceGender)

    def detectAge(self):
        img_blob = cv2.dnn.blobFromImage(self.faceCropped)
        am = AgeModel()
        self.faceAge = am.startModel(img_blob)
        # return self.faceAge
        print(self.faceAge)

    def saveImage(self):
        self.path = 'faces/camera_' + str(self.camNum) + '/id_' + str(self.id) + '_age_' + str(
            self.faceAge) + '_gender_' + self.faceGender + '.jpg'
        cv2.imwrite(self.path, self.faceCropped)

    def sendImage(self):
        img = open(self.path, 'rb')
        date = datetime.now().strftime("%I:%M %p")
        x = nt.uploadFun(img, self.faceAge, self.faceGender, date, self.camNum)
        print(x)
