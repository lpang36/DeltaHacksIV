import MySQLdb
import numpy as np
import pandas
from tqdm import tqdm

max_y = 37.821
min_y = 37.707
max_x = -122.365
min_x = -122.513
mesh = 0.002

key = open('key.txt','r')
pw = key.read().replace('\n','')
db = MySQLdb.connect(host='localhost',
                             user='root',
                             passwd=pw,
                             db='crime')

df = pandas.DataFrame(columns=['X','Y','Count'])
cur = db.cursor()
#cur.execute('CREATE TABLE sf_graph (X DECIMAL(12,9), Y DECIMAL(12,9), Count INT);')
for i in tqdm(np.arange(min_x,max_x,mesh)):
  for j in np.arange(min_y,max_y,mesh):
    cur.execute('SELECT COUNT(Id) FROM san_francisco WHERE ABS(X - '+str(i)+')<'+str(mesh)+' AND ABS(Y - '+str(j)+')<'+str(mesh))
    row = cur.fetchall()
    df = df.append({'X':i,'Y':j,'Count':row[0][0]},ignore_index=True)
    
db.close()
df.to_csv('graph.csv')