import asyncio

STOPPED_SEARCHING= 100
SEARCHING_DRIVING= 140
DRIVING_SEARCHING= 100
ANY_STOPPED= 50

def publishDistance(left,right):
  return {'left': left, 'right': right}

async def fakeCamera():
  while True:
    await asyncio.sleep(2)
    print('transition to searching')
    yield publishDistance(STOPPED_SEARCHING+10,STOPPED_SEARCHING+10)
    await asyncio.sleep(2)
    print('transition to driving')
    yield publishDistance(SEARCHING_DRIVING+10,SEARCHING_DRIVING+10)
    await asyncio.sleep(2)
    print('transition to searching')
    yield publishDistance(DRIVING_SEARCHING-10,DRIVING_SEARCHING-10)
    print('transition to stopped')
    await asyncio.sleep(2)
    yield publishDistance(ANY_STOPPED-10,ANY_STOPPED-10)
