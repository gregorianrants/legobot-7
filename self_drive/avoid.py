from constants import MODES,ACTIONS,SIDES,TRANSITIONS


#todo consider renamin this function
def updatePositionState(state,left,right):
  state = state.copy()
  state.minValue = min(left,right)
  # state.closestSide =  left <= right ? 'left' : 'right'
  state.closestSide =  'left' if left <= right else 'right'
  return state


def getPivotDirection(state):
  closestSide = state.closestSide
  print(closestSide)
  if closestSide==SIDES.LEFT:
    return ACTIONS.PIVOT_RIGHT
  
  if closestSide==SIDES.RIGHT:
    return ACTIONS.PIVOT_LEFT
  
  #return action


def updateStopedState(newState,previousState):
  STOPPED_SEARCHING = TRANSITIONS.STOPPED_SEARCHING
  newState = newState.copy()
  if newState.minValue> STOPPED_SEARCHING:
    newState.mode = MODES.SEARCHING
    newState.action = getPivotDirection(newState)
    return newState
  return newState

def updateBackState(newState):
  print('in update back state')
  newState = newState.copy()
  if newState.minValue> TRANSITIONS.BACK_SEARCHING:
    newState.mode = MODES.SEARCHING
    newState.action = getPivotDirection(newState)
    print(newState.action)
    return newState
  return newState


def updateSearchingState(newState):
  SEARCHING_DRIVING = TRANSITIONS.SEARCHING_DRIVING
  newState = newState.copy()
  if(newState.minValue>SEARCHING_DRIVING):
    newState.mode = MODES.DRIVING
    newState.action = ACTIONS.FORWARD  
  return newState


def updateDrivingState(newState):
  DRIVING_SEARCHING = TRANSITIONS.DRIVING_SEARCHING
  newState = newState.copy()
  if newState.minValue<DRIVING_SEARCHING:
    newState.mode = MODES.SEARCHING
    newState.action = getPivotDirection(newState)
  return newState

def reducer(state,left,right):
  previousState = state
  newState = updatePositionState(state,left,right)
  if newState.minValue<=TRANSITIONS.ANY_BACK:
    newState.mode=MODES.BACK
    newState.action = ACTIONS.BACK
    return newState
  if previousState.mode == MODES.BACK:
    return updateBackState(newState)
  if previousState.mode == MODES.STOPPED:
    return updateStopedState(newState,previousState)
  if previousState.mode == MODES.SEARCHING:
    return updateSearchingState(newState)
  if previousState.mode ==MODES.DRIVING: 
    return updateDrivingState(newState)
  
  
  return newState


# we maintain state in here rather than using state from user of module as we require the previous state to make updates
# this may not be strictly necessary,

class State:
  def __init__(self,mode=MODES.STOPPED,minValue=None,closestSide=None,action=None):
    self.mode = mode
    self.minValue = minValue
    self.closestSide = closestSide
    self.action =action

  def __str__(self) -> str:
    return str(vars(self))

  def copy(self):
    return State(self.mode,self.minValue,self.closestSide,self.action)
  

class  Store():
  state = State()

  def getState(self):
    return self.state

  def updateState(self,left,right):
    self.state = reducer(self.state,left,right)


# store = Store()

# updateState = store.updateState
# getState = store.getState

# print(TRANSITIONS.ANY_STOPPED)

# print(getState())
# updateState(150,150)
# print(vars(getState()))
# updateState(80,150)
# print(getState())
# updateState(150,150)
# print(getState())
# updateState(10,150)
# print(getState())



