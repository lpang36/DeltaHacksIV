import numpy as np
from heapq import heappush, heappop

"""
max_y = 37.821
min_y = 37.707 #latitude
max_x = -122.365
min_x = -122.513"""

def findNearestNeighbours(interval,center,min,max,grid):
    "find the nearest neighbours given the min and max coordinates, grid and the 'center node'"
    #x values
    ans = []
    bound_min = []
    bound_min.append(center[0] - interval)
    bound_min.append(center[1] - interval)

    bound_max = []
    bound_max.append(center[0] + interval)
    bound_max.append(center[1] + interval)

    #print(center)
    #print(bound_min)
    #print(bound_max)

    for i in range(min[0],max[0]):
        for j in range(min[1],max[1]):
            if (i >= bound_min[0] and i <= bound_max[0]) and (j >= bound_min[1] and j <= bound_max[1]):
                tempCoor = (i,j)
                ans.append(tempCoor)

    return ans

def dist(finish,current):
    Val = ((finish[0] - current[0])**2 + (finish[1] - current[1])**2)**0.5
    return Val

def withCrime(current,finish)
    return dist(current,finish) + #INSERT CRIMES HERE

def path(cmFrom,current):
    total = [current]
    while current in cmFrom:
        current = cmFrom[current]
        total.append(current)
    return total

def astar(start,finish):
    "a star algorithm"

    """if start in closedSet: #if already visited
        return
    else: #add neighbours and pop top off the priority queue
        neigh = findNearestNeighbours(1,start,(0,0),(9,9),grid)
        for i in neigh:
            heappush(heap,(heuristic(start,finish,i),i))
        temp = heappop(heap)
        if temp == finish:
            return """
    closedSet = []
    openSet = [start]
    cmFrom = {}
    gScore = {}
    gScore[start] = 0
    fScore = {}
    fScore[start] = dist(start,finish)

    while openSet:
        tempMin = fScore[openSet[0]]
        current = openSet[0]
        for i in openSet:
            print(i)
            print("temp")
            print(tempMin)
            print("score")
            print(fScore[i])
            if fScore[i]<tempMin:
                current = i
                tempMin = fScore[i]

        if current == finish:
            return path(cmFrom,current)
        openSet.remove(current)
        closedSet.append(current)

        for i in findNearestNeighbours(1,current,(0,0),(9,9),grid):
            if i in closedSet:
                continue
            else:
                openSet.append(i)
            tempGScore = gScore[current] + dist(current,i)
            print(i)
            print(tempGScore)
            if i in gScore:
                if tempGScore <= gScore[i]:
                    cmFrom[i] = current
                    gScore[i] = tempGScore
                    fScore[i] = gScore[i] + withCrime(i,finish)
            else:
                cmFrom[i] = current
                gScore[i] = tempGScore
                fScore[i] = gScore[i] + withCrime(i,finish)


grid = np.empty((0,10))
for i in range(0,10):
    temp = np.arange(10)
    grid = np.vstack((grid,temp))

#print(grid)
#print(findNearestNeighbours(1,(2.5,2.5),(0,0),(9,9),grid))
#print(heuristic((0.0,0.0),(5.0,5.0),(8,2.5)))

print(astar((1,2),(5,1)))
