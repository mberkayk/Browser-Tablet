import numpy as np
import cv2 as cv
from PIL import Image
from flask import Flask, render_template, Response
import pyautogui
from flask_socketio import SocketIO, emit
import time

class ScreenCap():
	def __init__(self):
		pass
	
	def capture(self):
		img = pyautogui.screenshot() 
		frame = np.array(img) 
		frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB) 
		time.sleep(0.010)
		ret, jpeg = cv.imencode('.jpg', frame)
		return jpeg.tobytes()


screenCap = ScreenCap()
app = Flask(__name__)
socketio = SocketIO(app)
	
	
def gen():
	while True:
		frame = screenCap.capture()
		yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
		

@app.route('/video_feed')
def video_feed():
	return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
	return render_template('index.html')

@socketio.on('message')
def handle_message(data):
  print('received message: ' + data)

@socketio.on('connect')
def test_connect():
  print('client connected')

@socketio.on('disconnect')
def test_disconnect():
  print('Client disconnected')

@socketio.on('mouseEvent')
def mouseEvent(x, y, p):
  print(x, y, p)


# app.run(host='0.0.0.0',port='8000', debug=True)
socketio.run(app, host='0.0.0.0',port='8000', debug=True)


