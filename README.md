# Palantir

Code to support an animal tracking device based on raspberry pi zero w and a camera with night vision. 

# Components used in the project:

- https://www.raspberrypi.org/products/raspberry-pi-zero-w/
- https://www.waveshare.com/wiki/RPi_IR-CUT_Camera
- https://www.dexterindustries.com/product/grovepizero/
- http://www.seeedstudio.com/depot/Grove-TempHumiBarometer-Sensor-BME280-p-2653.html
- http://wiki.seeedstudio.com/Grove-PIR_Motion_Sensor/

# Camera night mode
Add "disable_camera_led=1" to /boot/config.txt

or

Connect the GPIO from your Pi to the small hole on the right of the camera, and toggle modes by changing the GPIO logic level. (HIGH --> Normal Mode, LOW --> Night-vision Mode)

# Convert video to mp4
scp pi@raspberrypi.local:palantir/video.h264 Desktop/ && MP4Box -add Desktop/video.h264 Desktop/pivideo.mp4 && rm Desktop/video.h264
