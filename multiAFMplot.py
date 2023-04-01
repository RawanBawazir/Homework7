import matplotlib.pyplot as plt
import numpy as np
import sys


filenames = sys.argv[1:]

## First Part

first_file=np.loadtxt(filenames[0], delimiter=',').shape

n=len(filenames)
surface=np.zeros((n, first_file[0]))


for f in range(n):
    
    file_=np.loadtxt(filenames[f], delimiter=',')
    mean=file_.mean(axis=1)
    surface[f,:] = mean


plt.plot(surface.mean(axis=0))
plt.ylabel('Average Surface Map')
plt.savefig('mean_surface.png')
plt.show()


## Second Part

height=np.zeros((n, first_file[1]))


for f in range(n):
    
    file_=np.loadtxt(filenames[f], delimiter=',')
    mean=file_.mean(axis=0)
    height[f,:] = mean
    plt.plot(mean, alpha=0.3, color='green')
plt.plot(height.mean(axis=0), color='green')
plt.savefig('surface_compare.png')
plt.ylabel('Average Height Map')
plt.show()
