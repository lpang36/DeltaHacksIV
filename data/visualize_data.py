import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

arr = np.reshape(np.loadtxt('altered_graph.csv',delimiter=','),(-1))
x = [[0]*75 for i in range(57)]
y = [[0]*75 for i in range(57)]
for i in range(57):
  for j in range(75):
    x[i][j] = i
for i in range(75):
  for j in range(57):
    y[j][i] = i
indx = np.reshape(np.array(x),(-1))
indy = np.reshape(np.array(y),(-1))
fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')
ax1.bar3d(indx,indy,np.zeros_like(arr),np.ones_like(arr),np.ones_like(arr),arr)
plt.show()