from constants import MODES,ACTIONS
from client import distance_gen
import asyncio
from avoid import Store
from fakeCamera import fakeCamera

import sys
sys.path.append('../legobot-7')
from SelfCorrectingRobot import SelfCorrectingRobot

class SelfDrive:
  def __init__(self,motors,distance_gen):
    self.previousAction = None
    self.nextAction = ACTIONS.STOP
    self.running = False
    self.motors = motors
    self.store = Store()
    self.distance_gen = distance_gen
          
  def resetState(self):
    #self.store = store()
    self.previousAction = None
    self.nextAction = ACTIONS.STOP

  def handleNewData(self,left,right):
    self.store.updateState(left,right)
    self.nextAction = self.store.getState().action
    
    if self.nextAction!=self.previousAction:
            print(self.store.getState())
            self.handleAction()
            self.previousAction = self.nextAction
          
  def handleAction(self):
    if self.nextAction == ACTIONS.FORWARD:
      self.motors.forward(50)
    
    if self.nextAction ==ACTIONS.PIVOT_LEFT:
      self.motors.pivot_left(50)
    
    if self.nextAction ==ACTIONS.PIVOT_RIGHT:
      self.motors.pivot_right(50)

    if self.nextAction ==ACTIONS.BACK:
      self.motors.backward(50)
    
    if self.nextAction ==ACTIONS.STOP:
      self.motors.stop()
          

  async def start(self):
    self.running = True
    async for distance in self.distance_gen():
      if self.running == False: 
        self.motors.stop()
        self.reset()
        break
      self.handleNewData(distance['left'],distance['right'])

  def stop(self):
      self.running = False

  

motors = SelfCorrectingRobot()

self_drive = SelfDrive(motors,distance_gen)

async def main():
  start = asyncio.create_task(self_drive.start())
  start_robot = asyncio.create_task(motors.start())
  await start


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('asdfsadfsadf')
    self_drive.stop()
    motors.stop()
finally:
    self_drive.stop()
    motors.stop()

motors.stop()



  

