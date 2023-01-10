from adafruit_motorkit import MotorKit


class Robot:
        def __init__(self):
                self.kit = MotorKit()
                self.left_motor = self.kit.motor1
                self.right_motor = self.kit.motor2
                

        def convert_speed(self,speed):
                return speed/100

        def set_left(self,speed):
                self.left_motor.throttle = self.convert_speed(speed)

        def set_right(self,speed):
                self.right_motor.throttle = self.convert_speed(speed)

        def set_both(self,speed):
                self.set_left(speed)
                self.set_right(speed)

        def stop(self):
                self.set_both(0)

        def forward(self,speed):
                self.set_both(speed)

        def backward(self,speed):
                self.set_both(-speed)

        def pivot_left(self,speed):
                self.set_left(-speed)
                self.set_right(speed)

        def pivot_right(self,speed):
                self.set_left(speed)
                self.set_right(-speed)
