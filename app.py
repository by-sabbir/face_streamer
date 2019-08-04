import os
import json
from camera import VideoCamera
from flask import Flask, render_template, redirect, Response, url_for, session


base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'face_streamer'


@app.route('/')
def index():
    return render_template('index.html')


def gen(camera):
    while True:
        ifFace, frame = camera.get_frame()
        if frame is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/face')
def face():
    file_name = os.path.join(base_dir, 'static/face_state.json')
    with open(file_name, 'r') as face:
        data = json.loads(face.read())
    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True)
