xvel=1
yvel=1

currenthigh = 0
highFound = False

hitCo = []

def processVel (velx,vely,currentx,currenty):
    # targetxmin=20
    # targetxmax=30
    # targetymin=-10
    # targetymax=-5
    
    targetxmin=137
    targetxmax=171
    targetymin=-98
    targetymax=-73

    highPoint = 0
    for step in range(1,500):
        if (not targetxmin <= currentx <= targetxmax) or (not targetymin <= currenty <= targetymax):
            currentx += velx
            currenty += vely
            if velx > 0:
                velx -=1
            elif velx < 0:
                velx += 1
            else:
                velx = 0
            vely -= 1
            if currenty > highPoint:
                highPoint = currenty
        else:
            return {'result':True, 'maxHeight':highPoint}
    return {'result':False, 'maxHeight':highPoint}

for x in range(1,500):
    for y in range(-500,500):
        result = processVel(x,y,0,0)
        if result['result']:
            if result['maxHeight'] > currenthigh:
                currenthigh = result['maxHeight']
            hitCo.append(str(x)+','+str(y))
            
print ('Number of Hits', str(len(hitCo))) 
print('High Point ' + str(currenthigh))



