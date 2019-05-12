import bme280
import picamera
import time 
import grovepi

class Palantir:
    def __init__(self, resolution = (1920, 1080), framerate = 30, rotation = 0):
        self.camera = picamera.PiCamera()
        self.camera.resolution = resolution
        self.camera.framerate = framerate
        self.camera.rotation = rotation

    def take_picture(self, filename, annotation=None):
        self.camera.start_preview()
        if annotation is not None:
            self.camera.annotate_text = annotation
        time.sleep(2)
        self.camera.capture(filename)

    def take_video(self, filename, duration = 10, annotation = None):
        if annotation is not None:
            self.camera.annotate_text = annotation
        time.sleep(2)
        self.camera.start_recording(filename)
        self.camera.wait_recording(duration)
        self.camera.stop_recording()

class Environment:

    def get_env_info(self):
        temperature,pressure,humidity = bme280.readBME280All()
        return 'Temp: {:.1f}C, Pres: {:.0f} hPa, Hum: {:.2f}%'.format(temperature, pressure, humidity)

def wait_for_motion():
    pir_sensor = 3
    motion = 0
    grovepi.pinMode(pir_sensor, 'INPUT')
    
    env = Environment()
    palantir = Palantir(rotation = 180)

    while True:
        try:
            motion = grovepi.digitalRead(pir_sensor)
            if motion == 0 or motion == 1: #it could be 255 because of IO Errors
                if motion == 1:
                    print('Say Cheese!')
                    #take_picture('foo.jpg', take_env_info())
                    palantir.take_video('video.h264', duration = 10, annotation = env.get_env_info())
                    exit(0)
            time.sleep(.2)
        except IOError:
            print('Error')

def main():
    wait_for_motion()
    
if __name__=="__main__":
    main()
    
