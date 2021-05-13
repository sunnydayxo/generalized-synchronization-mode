
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#define universal variables
c0 = 15.6
c1 = 28.0
m0 = -1.143
m1 = -0.714
def f(x):
    f = m1*x+(m0-m1)/2.0*(abs(x+1.0)-abs(x-1.0))
    return f
def dH_dt(H, t=0):
    return np.array([c0*(H[1]-H[0]-f(H[0])),
                  (H[0]-H[1]+H[2]),
                  -c1*H[1]])
t = np.linspace(0, 100, 10000)
#x, y, and z initial conditions
H0 = [0.0001, 0.0001, 0.0001]
H, infodict = integrate.odeint(dH_dt, H0, t, full_output=True)



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(H[:,0], H[:,1], H[:,2])
plt.show()
