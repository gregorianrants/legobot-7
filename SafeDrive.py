import time


class SafeDrive:
  def __init__(self,motors,distance_gen):
    self.BACKWARDS = 'BACKWARDS'
    self.SAFE= 'SAFE'
    self.UNSAFE = 'UNSAFE'
    self.state = self.UNSAFE
    self.motors = motors
    self.time_of_state_change = None
    self.running = True
    self.distance_gen = distance_gen

  def updateBackwards(self):
    finished = (time.time()-self.time_of_state_change)>1
    if(finished):
      self.motors.stop()
      self.state = self.UNSAFE

  def startBackwards(self,speed):
    self.state = self.BACKWARDS
    self.time_of_state_change = time.time()
    self.motors.backward(speed)

  def handleNewData(self,left,right):
    if (self.state == self.BACKWARDS):
      self.updateBackwards()
    elif(left<40 or right <40):
      self.motors.stop()
      self.state = self.UNSAFE
    else:
       self.state = self.SAFE

  def stop(self):
    self.motors.stop()

  def forward(self,speed):
    if(self.state == self.SAFE):
      self.motors.forward(speed)

  def backward(self,speed):
     self.startBackwards(speed)

  def pivot_left(self,speed):
     if(self.state == self.SAFE):
      self.motors.pivot_left(speed)

  def pivot_right(self,speed):
     if(self.state == self.SAFE):
      self.motors.pivot_right(speed)

  async def start(self):
    self.running = True
    async for distance in self.distance_gen():
      if self.running == False: 
        self.motors.stop()
        self.reset()
        break
      self.handleNewData(distance['left'],distance['right'])
