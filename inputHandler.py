import bge
from bge import logic,events
path=logic.expandPath("//")
bge.render.showMouse(1)
def start(cont):
    l_click = cont.sensors['MouseStart']
    m_over = cont.sensors['MouseStart1']
    game_actuator = cont.actuators['startGame']
    if l_click.positive and m_over.hitObject:
        cont.activate(game_actuator)
        #cont.activate(startGame)
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
        if len(input)==3 or len(input)==7:
            own["userInput"]+="\n"
    else:
        return
def show(cont):
    value=[]
    for sens in cont.sensors:
        if not sens.positive:
            return
    input=value1   
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
