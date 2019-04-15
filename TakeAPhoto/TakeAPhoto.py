import picamera

#setup the camera  (it closes when we are done with it)
print("smile")
with picamera.PiCamera() as camera:
    camera.resolution = (1280,720)
    camera.capture("//home/pi/Desktop/innovationProject/innovationProject/TakeAPhoto/newimage.jpg")
print("done")
