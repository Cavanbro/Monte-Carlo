import random
import math
import numpy as np
import matplotlib.pyplot as plt

## Creating plot and defining points inside/outside
N = 1000
coords = np.random.rand(N, 2)
coords_inside = np.zeros((N, 2))
coords_outside = np.zeros((N, 2))

def find_R(x, y):
    r = math.sqrt(x**2 + y**2)
    return r

for i in range(N):
     r = find_R(coords[i,0], coords[i,1])
     if r<=1:
         coords_inside[i] = ([coords[i,0], coords[i,1]])
     else:
         coords_outside[i] = ([coords[i,0], coords[i,1]])

coords_inside_trimmed = np.delete(coords_inside, np.where((coords_inside==0).all(axis=1)), axis=0)
coords_outside_trimmed = np.delete(coords_outside, np.where((coords_outside==0).all(axis=1)), axis=0)

plt.plot(coords_inside_trimmed[:, 0], coords_inside_trimmed[:, 1], 'o', color='r')
plt.plot(coords_outside_trimmed[:, 0], coords_outside_trimmed[:, 1], 'o', color='b')
plt.axis('square')
plt.show()


## Calculating pi with points
n_inside = len(coords_inside_trimmed)
n_outside = len(coords_outside_trimmed)

A = n_inside/(n_inside+n_outside)
print(A * 4)
