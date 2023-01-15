class SafeDrive:
  def __init__(self,motors,distance_gen):
    self.safe = False
    self.motors = motors

  def handleNewData(self,left,right):
    if(left<40 or right <40):
      motors.stop()
      self.safe = False
    else:
      self.safe = True


  async def start(self):
    self.running = True
    async for distance in self.distance_gen():
      if self.running == False: 
        self.motors.stop()
        self.reset()
        break
      self.handleNewData(distance['left'],distance['right'])
