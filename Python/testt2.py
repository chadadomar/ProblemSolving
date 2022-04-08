from __future__ import division
from scipy import *
from pylab import *

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D # librairie 3D

# Type de l'onde
E0y = 1
E0z = 1
phi = pi/2
T = 125

fig = figure()
ax = fig.gca(projection='3d')

x,y,z = array([]), array([]), array([])

for i in range(301):
    x_fin=i
    y_fin=E0y * cos(2*pi*i/T)
    z_fin=E0z * cos(2*pi*i/T-phi)
    plot([i,x_fin], [0,y_fin], [0,z_fin],color='b')     # Champ E
    
    x = append(x,x_fin)
    y = append(y,y_fin)
    z = append(z,z_fin)

plot(x, y, z,color='b',lw=2)    # Contour du Champ E (paramétrique 3D)
show()