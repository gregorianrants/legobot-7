from gpiozero import DigitalInputDevice
import time

class EncoderCounter(object):
  def __init__(self,pin_number,side):
    self.side = side
    self.test_mode = False
    self.pulse_count = 0
    self.device = DigitalInputDevice(pin=pin_number)
    self.device.pin.when_changed = self.count_pulses
    self.previous = None
    self.difs = []

  def record_gap_between_high(self,_,state):
    if(state == 1):
        if self.previous==None:
          self.previous = time.time()
        else:
          next = time.time()
          dif = next-self.previous
          self.previous = next
          self.difs.append(dif)

  def count_pulses(self,_,state):
    self.pulse_count +=1

  def reset(self):
    self.pulse_count=0

  def set_mode(self,mode):
    if(mode=='normal'):
      self.test_mode = False
      self.device.pin.when_changed = self.count_ticks
    if(mode=='test'):
      self.test_mode = True
      self.device.pin.when_changed = self.record_gap_between_high

  def report_test(self,np):
    result = np.array(self.difs)
    result = result[20:-20]
    centred = result - result.mean()
    centred = np.absolute(centred)
    sd = result.std()
    outliers = result[centred>sd*2]
    print(f'result for side: {self.side}')
    print(f'max: {result.max()}, min: {result.min()}, mean {result.mean()} , sd {result.std()}')
    print('outliers',outliers)
    return result
   

# bot.stop()


