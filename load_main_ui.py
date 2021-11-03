import os
from Models.matching.matching import startMatching
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from Models.detection.Detection import *
import threading

# 1920*1080 {30%1920*50%1080}
current_dir = os.path.dirname(os.path.abspath(__file__))
MainUI, Base = uic.loadUiType(os.path.join(current_dir, "ui//main_ui.ui"))


class Thread(QtCore.QThread):
    ImageUpdate_0 = QtCore.pyqtSignal(QtGui.QImage)
    ImageUpdate_1 = QtCore.pyqtSignal(QtGui.QImage)
    ImageUpdate_2 = QtCore.pyqtSignal(QtGui.QImage)
    ImageUpdate_3 = QtCore.pyqtSignal(QtGui.QImage)
    ImageUpdate_4 = QtCore.pyqtSignal(QtGui.QImage)

    def run(self):
        self.ThreadActive = True
        #capture_0 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        #capture_1 = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        #capture_2 = cv2.VideoCapture(2, cv2.CAP_DSHOW)
        # capture_3 = cv2.VideoCapture(3, cv2.CAP_DSHOW)
        capture_3 = cv2.VideoCapture('data/Face detection.mp4')
        #capture_4 = cv2.VideoCapture(4, cv2.CAP_DSHOW)
        # capture = cv2.VideoCapture('data/1920_stock-photo-mosaic-of-satisfied-people-157248584.jpg')
        while self.ThreadActive:
            # camera 0
            # ret_0, frame_0 = capture_0.read()
            # if ret_0:
            #     flippedImage = self.readyFrame(frame_0)
            #     # flippedImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #     detection = Detection()
            #     flippedImage = detection.faceTracking(flippedImage, 0)
            #     # ------------------------------------------------------------ #
            #     pic = self.converttoQTformat(flippedImage)
            #     # print(pic.width(), '\t', pic.height(), '\n', type(pic))
            #     self.ImageUpdate_0.emit(pic)
            #
            # # camera 1
            # ret_1, frame_1 = capture_1.read()
            # if ret_1:
            #     flippedImage = self.readyFrame(frame_1)
            #     # flippedImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #     detection = Detection()
            #     flippedImage = detection.faceTracking(flippedImage, 1)
            #     # ------------------------------------------------------------ #
            #     pic = self.converttoQTformat(flippedImage)
            #     # print(pic.width(), '\t', pic.height(), '\n', type(pic))
            #     self.ImageUpdate_1.emit(pic)
            #
            # # camera 2
            # ret_2, frame_2 = capture_2.read()
            # if ret_2:
            #     flippedImage = self.readyFrame(frame_2)
            #     # flippedImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #     detection = Detection()
            #     flippedImage = detection.faceTracking(flippedImage, 2)
            #     # ------------------------------------------------------------ #
            #     pic = self.converttoQTformat(flippedImage)
            #     # print(pic.width(), '\t', pic.height(), '\n', type(pic))
            #     self.ImageUpdate_2.emit(pic)
            #
            # # camera 3
            ret_3, frame_3 = capture_3.read()
            # frame_3=cv2.imread('data/1920_stock-photo-mosaic-of-satisfied-people-157248584.jpg')
            if ret_3:
                flippedImage = self.readyFrame(frame_3)
                # flippedImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                detection = Detection()
                flippedImage = detection.faceTracking(flippedImage, 3)
                # ------------------------------------------------------------ #
                pic = self.converttoQTformat(flippedImage)
                # print(pic.width(), '\t', pic.height(), '\n', type(pic))
                self.ImageUpdate_3.emit(pic)

            # camera 4
            # ret_4, frame_4 = capture_4.read()
            # if ret_4:
            #     flippedImage = self.readyFrame(frame_4)
            #     # flippedImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #     detection = Detection()
            #     flippedImage = detection.faceTracking(flippedImage, 4)
            #     # ------------------------------------------------------------ #
            #     pic = self.converttoQTformat(flippedImage)
            #     # print(pic.width(), '\t', pic.height(), '\n', type(pic))
            #     self.ImageUpdate_4.emit(pic)

    def readyFrame(self, frame):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        flippedImage = cv2.flip(image, 1)
        return flippedImage

    def converttoQTformat(self, image):
        converted = QtGui.QImage(image.data, image.shape[1], image.shape[0],
                                 QtGui.QImage.Format_RGB888)
        pic = converted.scaled(630, 470, QtCore.Qt.KeepAspectRatio)  # 4 : 3
        return pic

    def stop(self):
        self.ThreadActive = False
        self.quit()


class Main(Base, MainUI):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        # self.center_main_window()
        self.thread = Thread()
        self.thread.start()
        self.thread.ImageUpdate_0.connect(self.imageUpdateSlot_0)
        self.thread.ImageUpdate_1.connect(self.imageUpdateSlot_1)
        self.thread.ImageUpdate_2.connect(self.imageUpdateSlot_2)
        self.thread.ImageUpdate_3.connect(self.imageUpdateSlot_3)
        self.thread.ImageUpdate_4.connect(self.imageUpdateSlot_4)

    def imageUpdateSlot_0(self, image):
        self.camera_0.setPixmap(QtGui.QPixmap.fromImage(image))

    def imageUpdateSlot_1(self, image):
        self.camera_1.setPixmap(QtGui.QPixmap.fromImage(image))

    def imageUpdateSlot_2(self, image):
        self.camera_2.setPixmap(QtGui.QPixmap.fromImage(image))

    def imageUpdateSlot_3(self, image):
        self.camera_3.setPixmap(QtGui.QPixmap.fromImage(image))

    def imageUpdateSlot_4(self, image):
        self.camera_4.setPixmap(QtGui.QPixmap.fromImage(image))

    def center_main_window(self):
        # geometry of the main window
        qr = self.frameGeometry()
        # print(self.frameGeometry().width(),self.frameGeometry().height())
        # center point of screen
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()

    window.show()
    # window.center_main_window()
    window.showMaximized()
    # app.processEvents()
    t = threading.Thread(target=startMatching, args=())
    t.start()
    sys.exit(app.exec_())
