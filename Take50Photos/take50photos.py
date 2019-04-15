import picamera

def Main():
    i = 0
    img = 'img'
    while (i != 50):
        with picamera.PiCamera() as camera:
            print(i)
            camera.resolution = (640,720)
            camera.capture("/home/pi/Desktop/innovationProject/innovationProject/Take50Photos/{}.jpg".format(img+str(i)))
        i += 1

if __name__ == '__main__':
    Main()
    
