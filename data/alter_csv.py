import pandas
import numpy as np

df = pandas.read_csv('graph.csv')
max_y = 37.821
min_y = 37.707
max_x = -122.365
min_x = -122.513
mesh = 0.002

n = len(np.arange(min_y,max_y,mesh))
m = len(np.arange(min_x,max_x,mesh))
arr = np.zeros((n,m))

for i in range(len(df)):
  arr[i%n][i/n] = df['Count'][i]
np.savetxt('altered_graph.csv',arr,delimiter=',')