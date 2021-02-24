import numpy as np
import cv2 as cv
from PIL import Image
from flask import Flask, render_template, Response
import pyautogui
from threading import Thread
import time



class ScreenCap():
	def __init__(self):
		self.resolution = (1920, 1080) 
		self.codec = cv.VideoWriter_fourcc(*"XVID") 
		self.fps = 60.0

	
	def capture(self):
		img = pyautogui.screenshot() 
		frame = np.array(img) 
		frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB) 
		time.sleep(0.010)
		ret, jpeg = cv.imencode('.jpg', frame)
		return jpeg.tobytes()


screenCap = ScreenCap()
app = Flask(__name__)
	
	
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




app.run(host='0.0.0.0',port='8000', debug=True)
 


