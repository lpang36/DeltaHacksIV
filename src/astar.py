import numpy as np
import heapq
import pandas

def coord_to_ind(coord,x,y,mesh=0.002):
    return (round((coord[0]-x[0])/mesh),round((coord[1]-y[0])/mesh))
  
def ind_to_coord(ind,x,y,mesh=0.002):
    return (round(ind[0]*mesh+x[0],3),round(ind[1]*mesh+y[0],3))

def findNearestNeighbours(cur,x,y):
    out = []
    for i in range(-1,2):
        for j in range(-1,2):
            if (i!=0 or j!=0) and cur[0]+i>=x[0] and cur[0]+i<x[1] and cur[1]+j>=y[0] and cur[1]+j<y[1]:
                out.append((cur[0]+i,cur[1]+j))
    return out

def dist(finish,current):
    Val = ((finish[0] - current[0])**2 + (finish[1] - current[1])**2)**0.5
    return Val
  
def crime(current,arr,weight=0.001):
    return arr[int(current[1])][int(current[0])]*weight

def path(cmFrom,current,x,y):
    total = [current]
    while current in cmFrom:
        current = cmFrom[current]
        total.append(current)
    for i in range(1,(len(total)-1)/2):
      temp = total[i]
      total[i] = total[len(total)-i-1]
      total[len(total)-i-1] = temp
    return [ind_to_coord(i,x,y) for i in total[1:(len(total)-1)]]

def astar(start_coord,finish_coord,x,y,dims,weight=0.001):
    start = coord_to_ind(start_coord,x,y)
    finish = coord_to_ind(finish_coord,x,y)
    arr = np.loadtxt('../data/altered_graph.csv',delimiter=',')
    
    "a star algorithm"
    closedSet = {}
    openSet = [(dist(start,finish),start)] #each element in openSet (a minheap) is a tuple: (f,(x,y))
    cmFrom = {}
    gScore = {}
    gScore[start] = 0
    fScore = {}
    fScore[start] = dist(start,finish)

    while openSet:
        current = heapq.heappop(openSet)
        for i in findNearestNeighbours(current[1],(0,dims[0]),(0,dims[1])):
            if i == finish:
                cmFrom[i] = current[1]
                return path(cmFrom,i,x,y)
            tempGScore = gScore[current[1]] + crime(i,arr,weight)
            tempFScore = tempGScore + dist(finish,i)
            if i in fScore and fScore[i]<=tempFScore:
                continue
            else:
                heapq.heappush(openSet,(tempFScore,i))
                gScore[i] = tempGScore
                fScore[i] = tempFScore
                cmFrom[i] = current[1]
        closedSet[current[1]] = True
