import requests
import MySQLdb
import heapq

def colinear(p1,p2,p3):
  if p1[0]==p2[0] or p1[0]==p3[0]:
    return p2[0]==p3[0]
  return (p2[1]-p1[1])/(p2[0]-p1[0])==(p3[1]-p1[1])/(p3[0]-p1[0])

def path_plan(x1,y1,x2,y2,weight,limit=23):
  key = "AIzaSyDqJhJm3UaQovwomgnS8XvEUqiQrVgRpj0"
  max_y = 37.821
  min_y = 37.707
  max_x = -122.365
  min_x = -122.513
  key = open('key.txt','r')
  pw = key.read().replace('\n','')
  db = MySQLdb.connect(host='localhost',
                             user='root',
                             passwd=pw,
                             db='crime')
  cur = db.cursor()
  
  #path simplification algorithm
  pts = [] #to be supplied by A* as a list of pairs
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