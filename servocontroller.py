from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory

class ServoController:
    """
    Controls the movement of the servo which locks and unlocks the snack box lid.
    """

    def __init__(self):
        self.factory = PiGPIOFactory()
        self.servo = Servo(17, pin_factory=self.factory)

    def open(self):
        self.servo.min()

    def close(self):
        self.servo.max()
