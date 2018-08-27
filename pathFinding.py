import bge
from bge import logic
path=logic.expandPath("//")
bge.render.showMouse(1)
def calculate():
    file=open(path+"values.txt",'r')
    info=file.readlines()
    global source,destination,velocity
    #reading source, destination and velocity
    source=str(info[0])
    destination=str(info[1])
    camera_velocity=str(info[2])
    #print(camera_velocity)
    cont1 = bge.logic.getCurrentController().actuators
    act=cont1[0]
    act.target=destination[0]+destination[1]+destination[2]     #target room
    act.velocity=int(camera_velocity)
    scene=bge.logic.getCurrentScene()
    door=scene.objects[source[0]+source[1]+source[2]]            #starting door
    door_location=door.worldPosition
    #print(door_location)
    camera=scene.objects["player_body"]
    camera.worldPosition=door_location

    nodes = ('225', '224', '223', '236', '235', '234', '233')
    distances = {
    '225': {'224': 1, '223': 2, '236': 4,'235':5,'234':6,'233':7},
    '224': {'225': 1, '223': 1, '236': 3,'235':4,'234':5,'235':6},
    '223': {'224': 1, '225': 2, '236': 2,'235':3,'234':4,'233':5},
    '236': {'223': 2, '224': 3, '225': 4,'235':1,'234':2,'233':3},
    '235': {'234': 1, '236': 2, '223': 4,'224':5,'225':6,'233':2},
    '234': {'235': 1, '233': 1, '236': 2,'223':4,'224':5,'225':6},
    '233': {'234': 1, '235': 2, '236': 3,'223':5,'224':6,'225':7}}

    unvisited = {node: None for node in nodes} 
    global visited
    visited = {}
    cont = bge.logic.getCurrentController()
    own = cont.owner

    current = source[0]+source[1]+source[2]
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    #print(visited)
def distance():
    print(visited)
    cont = bge.logic.getCurrentController()
    own = cont.owner
    new_destination=destination.replace("\n","")
    own.text=str(visited[new_destination])
    
