import bge
from bge import logic,events
path=logic.expandPath("//")
bge.render.showMouse(1)
#global source,destination,velocity
def start(cont):
    l_click = cont.sensors['MouseStart']
    m_over = cont.sensors['MouseStart1']
    game_actuator = cont.actuators['startGame']
    if l_click.positive and m_over.hitObject:
        cont.activate(game_actuator)
        #cont.activate(startGame)

"""def exit(cont):
    l_click = cont.sensors['MouseExit']
    m_over = cont.sensors['MouseExit1']
    game_actuator = cont.actuators['Game']
    if l_click.positive and m_over.hitObject:
        cont.activate(game_actuator)

"""
cont = bge.logic.getCurrentController()
own = cont.owner
def main():
    global keyEvents
    keyEvents=logic.keyboard.events
    hitKey=[k for k in keyEvents\
                    if keyEvents[k]==logic.KX_INPUT_JUST_ACTIVATED]
    #string=bge.events.EventToCharacter(hitKey[0],True)
  #  if hitKey!=[151] or hitKey!=[133] or hitKey!=[147] or hitKey!=[152] or hitKey!=[148] or hitKey!=[153] or hitKey!=[149] or hitKey!=[154] or hitKey!=[150] or hitKey!=[155] or hitKey!=[158]:
    #    return
    if hitKey==[133]:
        lenString=len(own["userInput"])
        oldString=own["userInput"]
        newString=oldString[0:len(oldString)-1]
        #print(lastChar)
        own["userInput"]=newString
        own.text=own["userInput"]
        print(newString)
    elif hitKey!=[]:
        #print(type(hitKey))
        value=bge.events.EventToCharacter(hitKey[0],True)
        own["userInput"]+=value
        own.text=own["userInput"]
        global value1
        value1=own["userInput"]
        input=own["userInput"]
        if len(input)>11:
            return
            #own["userInput"]+="value excedd"
        if len(input)==3 or len(input)==7:
            own["userInput"]+="\n"
    else:
        return
    #own.text=own["userInput"]
def show(cont):
    value=[]
    for sens in cont.sensors:
        if not sens.positive:
            return
    input=value1    #own["userInput"]
    for i in input:
        value.append(i)
    while "\n" in value:
            value.remove("\n")
    print(len(value))
    global source,destination,velocity
    source=''.join(str(i) for i in value[0:3])
    destination=''.join(str(i) for i in value[3:6])
    velocity=''.join(str(i) for i in value[6:len(value)])
    print(source)
    print(destination)
    print(velocity)

def save():
    file=open(path+"values.txt",'w')
    file.write(source+"\n"+destination+"\n"+velocity)
"""def back():
    #sensor=cont.sensors["keyboard"]
    for key,status in keyEvents.events:
        if status==bge.logic.KX_INPUT_JUST_ACTIVATED:
            string=bge.events.EventToString(key)
            if string=="BACKSPACEKEY":
                lenString=len(own["userInput"])
                oldString=own["userInput"]
                lastChar=oldString[lenString-1]
                own["userInput"]=oldString.rstrip(lastChar)
def main():
    
    mouseOver1=cont.sensors["mouseOver"]
    mouseClick=cont.sensors["mouseClick"]
    startGame=cont.actuators["startGame"]
    if mouseOver1.positive:
        own.color=[1,0,0,True]
        if mouseClick.positive:
            cont.activate(startGame)
    else:
        own.color=[0.8,0.8,0.8,True]

def exit():
    mouseClick=cont.sensors["mouseClick"]
    mouseOver=cont.sensors["mouseOver"]
    gameactu = cont.actuators['Game']
    if mouseOver.positive:
        own.color=[1,0,0,True]
        if mouseClick.positive:
            #bge.logic.setExitKey(113)
            cont.activate(gameactu) #
    else:
        own.color=[0.8,0.8,0.8,True]
        """

