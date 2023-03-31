import matplotlib.pyplot as plt
import numpy as np
import sys

filename = sys.argv[1]        # Stores ARG1 in filename, as in: $ python plot.py ARG1 ARG2 
data = np.loadtxt(filename, delimiter=',')   # Attempts to load filename into local variable data.

plot_name=filename.split('/')[-1].split('.')[0]


plt.imshow(data)
plt.title(f'{plot_name}')
plt.savefig(f'{plot_name}.png')
