
class Modes:
  def __init__(self):
    self.STOPPED = 'stopped'
    self.SEARCHING = 'searching'
    self.DRIVING = 'driving'
    self.BACK = 'back'

  def __str__(self) -> str:
    return vars(self)

class Actions:
  def __init__(self):
    self.BACK = 'back'
    self.FORWARD ='forward'
    self.STOP = 'stop'
    self.PIVOT_LEFT= 'pivot-left'
    self.PIVOT_RIGHT= 'pivot-right'
  def __str__(self) -> str:
    return vars(self)

class Sides:
  def __init__(self):
    self.LEFT= 'left'
    self.RIGHT= 'right'
  def __str__(self) -> str:
    return vars(self)

class Transitions:
  def __init__(self):
    self.ANY_BACK = 40
    self.STOPPED_SEARCHING= 100
    # self.STOPPED_BACK= 30
    self.BACK_SEARCHING = 50
    self.SEARCHING_DRIVING= 140
    #self.DRIVING_SEARCHING= 100
    self.DRIVING_SEARCHING= 80
    #self.ANY_STOPPED= 50
    # self.ANY_STOPPED= 40
    
  def __str__(self) -> str:
    return vars(self)




MODES = Modes()
ACTIONS = Actions()
SIDES = Sides()
TRANSITIONS = Transitions()