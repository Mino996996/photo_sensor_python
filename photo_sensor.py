### --- ステッピングモータ制御　--- ###

import RPi.GPIO as GPIO
import struct
import time
import sys

### --- 接続用パラメータ --- ###

GPIO_SensorINPUT = 18 # GPIO-NO
GPIO_SensorLightMode = 11 # GPIO-NO
GPIO.setmode(GPIO.BCM)               # GPIO-NO 指定
GPIO.setup(GPIO_SensorINPUT,GPIO.IN)       # GPIO INPUT 指定
GPIO.setup(GPIO_SensorLightMode,GPIO.OUT)       # GPIO INPUT 指定

GPIO.output(GPIO_SensorLightMode, True)

### --------------------------- ###

def checkSensor():
    while True:
        time.sleep(1)
        mtr_sts = GPIO.input(GPIO_SensorINPUT)
        print(mtr_sts)

        if GPIO.input(GPIO_SensorINPUT) == GPIO.HIGH :
            print("Sensor is High")

 

##################################
# メインプログラム
##################################

if __name__ == "__main__":
    checkSensor()
 
    GPIO.cleanup()