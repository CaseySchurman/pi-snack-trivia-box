from urllib import request
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import subprocess

class ServoController:
    def __init__(self):
        subprocess.run('sudo pigpiod')
        self.factory = PiGPIOFactory()
        self.servo = Servo(17, pin_factory=self.factory)

    def open(self):
        self.servo.min()

    def close(self):
        self.servo.max()
