import os
import cv2
import json

baseDir = os.path.abspath(os.path.dirname(__file__))
casc_file = os.path.join(baseDir, 'face.xml')


class VideoCamera():

    def __init__(self):
        self.casc = cv2.CascadeClassifier(casc_file)
        self.video = cv2.VideoCapture(0)
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        # for saving the image uncomment the below code and delete time string
        detectFace = False
        success, image = self.video.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        faces = self.casc.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5, minSize=(80, 80), flags=cv2.CASCADE_SCALE_IMAGE)
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                detectFace = True
                cr_img = image[y - 50: y + h + 40, x - 40: x + w + 40]
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        data = {'face': detectFace}
        json_file_name = os.path.join(baseDir, 'static/face_state.json')
        with open(json_file_name, 'w') as jf:
            jf.write(json.dumps(data))
        image = cv2.resize(image, (640, 480))
        ret, jpeg = cv2.imencode('.jpg', image)
        return (detectFace, jpeg.tobytes())


if __name__ == '__main__':
    print(baseDir)
