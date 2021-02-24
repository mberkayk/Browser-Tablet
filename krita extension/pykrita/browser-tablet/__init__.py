import krita
import numpy as np
import cv2 as cv
from PIL import Image
from flask import Flask, render_template, Response



app = Flask(__name__)
		
class BrowserTabletExtension(krita.Extension):
	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent


	def setup(self):
		pass

	def browser_tablet(self):
		print('asdfasdfasdf')
		app.run(host='0.0.0.0',port='8000', debug=True)

	def createActions(self, window):
		action = window.createAction('browser_tablet', 'Browser Tablet', 'tools/scripts')
		action.triggered.connect(self.browser_tablet)


	def getImage(self):
		canvas = Krita.instance().activeDocument()
		w,h = canvas.width(), canvas.height()

		image = canvas.pixelData(0,0,w,h)
		pilImage = Image.frombytes("RGBA",(w,h), image)
		npImage = np.array(pilImage)
		ret, jpeg = cv2.imencode('.jpg', npImage)
		return jpeg.tobytes()
    
    
    
krita_instance = krita.Krita.instance()
extension = BrowserTabletExtension(krita_instance)
krita_instance.addExtension(extension)
	
	
def gen(self):
    while True:
        frame = extension.getImage()
        yield (b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed(self):
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')
	
	
