from Encoder import EncoderCounter
import time
from pid_controller import PIController
from robot import Robot
import asyncio

class Counter():
  def __init__(self):
    self.count = 0
    self.previous_time = None
    self.previous_count = None
    self.ticks_per_second = None


  def tick(self,count):
    if self.previous_time==None and self.previous_count ==None:
      self.previous_time = time.time()
      self.previous_count = count

    elif time.time()-self.previous_time >=1:
      self.previous_time = time.time()
      self.ticks_per_second = count - self.previous_count
      self.previous_count = count
      print('ticks per second',self.ticks_per_second)

  def reset(self):
    self.count = 0
    self.previous_time = None
    self.previous_count = None
    self.ticks_per_second = None
      

      
class SelfCorrectingRobot():
  def __init__(self):
    self.robot = Robot()
    self.state = 'stopped'
    self.left_encoder = EncoderCounter(17,'left')
    self.right_encoder = EncoderCounter(16,'right')
    self.left_counter = Counter()
    self.right_counter = Counter()
    self.forward_speed = 60
    self.pid = PIController(proportional_constant=5, integral_constant=0.3)

  def forward(self,speed):
    self.forward_speed = speed
    self.reset()
    self.state = 'forward'
    self.robot.set_left(self.forward_speed)
    self.robot.set_right(self.forward_speed)

  def stop(self):
    self.state='stopped'
    self.robot.stop()
    self.reset()

  def backward(self,speed):
    self.reset()
    self.state = 'backward'
    self.robot.backward()
               
  def pivot_left(self,speed):
    self.reset()
    self.state = 'pivot_left'
    self.robot.pivot_left(speed)

  def pivot_right(self,speed):
    self.reset()
    self.state = 'pivot_right'
    self.robot.pivot_right(speed)
         
  def count(self):
    self.left_counter.tick(self.left_encoder.pulse_count)
    self.right_counter.tick(self.left_encoder.pulse_count)

  def reset(self):
    self.left_encoder.reset()
    self.right_encoder.reset()
    self.left_counter.reset()
    self.right_counter.reset()

  def update(self):
    if(self.state=='forward'):
      left = self.left_encoder.pulse_count
      right = self.right_encoder.pulse_count
      error = left-right
      adjustment = self.pid.get_value(error)
      left_speed = int(self.forward_speed-adjustment)
      right_speed = int(self.forward_speed + adjustment)
      self.robot.set_left(left_speed)
      self.robot.set_right(right_speed)
      self.count()

  async def start(self):
    while True:
      self.update()
      await asyncio.sleep(0.01)
    



