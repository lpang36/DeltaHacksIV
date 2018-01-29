import requests
import heapq
from astar import astar

def colinear(p1,p2,p3):
  if p1[0]==p2[0] or p1[0]==p3[0]:
    return p2[0]==p3[0]
  return (p2[1]-p1[1])/(p2[0]-p1[0])==(p3[1]-p1[1])/(p3[0]-p1[0])

def path_plan(start,finish,weight=0.001,limit=8):
  x1 = start[0]
  y1 = start[1]
  x2 = finish[0]
  y2 = finish[1]
  max_y = 37.821
  min_y = 37.707
  max_x = -122.365
  min_x = -122.513
  rows = 57
  cols = 75
  
  pts = astar(start,finish,(min_x,max_x),(min_y,max_y),(cols,rows),weight)
  
  #path simplification algorithm
  short = [(x1,y1)] #assuming first node not returned by A*
  for i in range(1,len(pts)):
    if not colinear(short[len(short)-1],pts[i],pts[i-1]):
      short.append(pts[i])
  short.append((x2,y2)) #assuming final node not returned by A*
  if len(short)<limit: #limit on waypoints
    return short
  q = (len(short)-1)/limit
  r = (len(short)-1)%limit
  out = []
  count = 0
  for i in range(limit+1):
    out.append(short[count])
    count+=q
    if i<r:
      count+=1
  return out