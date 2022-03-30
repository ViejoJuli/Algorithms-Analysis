#Bipartite: There is no edge that connects vertices of same set.
enemies = {
    1:[2,4],
    2:[1,3],
    3:[2],
    4:[1,5,6],
    5:[4,6,7],
    6:[4,5,8],
    7:[5,8],
    8:[6,7]
}

father={}
color ={}
for node in enemies.keys():
    color[node]=-1
    father[node]=node

def bfs(dic):
    color[1]=1
    queue=[1] #Define source in 1
    while len(queue)>0:
        print("lista padres actual: ",father)
        print("lista actual: ",queue)
        print("persona a revisar: ", queue[0])
        print("enemigos: ",enemies[queue[0]])
        for enemy in dic[queue[0]]:
            print("color persona: ",color[queue[0]], "color enemigo: ",color[enemy])
            if color[enemy]==-1: #Not Visited
                father[enemy]=queue[0]
                color[enemy]=1-color[queue[0]]
                queue.append(enemy)
            elif color[enemy]==color[father[enemy]]:
                #print (color[enemy],color[father[enemy]])
                #return False



