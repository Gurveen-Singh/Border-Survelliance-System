from flask import Flask, render_template, redirect, session, url_for, flash, request, logging, Response
import os
from camera import VideoCamera
import threading

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', title="ABOUT")

@app.route('/capture')
def capture():
    return render_template('capture.html', title="LIVE FEED")

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b' --frame\r\n '
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/live_feed')
def live_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
                
@app.route('/alarm') #code for alarm buzzer goes here
def alarm():
    return render_template('alarm.html', title='ALARM')


if __name__ == '__main__':
    app.secret_key='12345secret'
    app.run(debug=True, port=80, host='0.0.0.0')

