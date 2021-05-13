import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#define universal variables
с0 = 0.0036
c1 = 10
c11=7
c3 = 3
m0=1
m1=2
m=m0/m1
def f(x):
    f = ((-m)*x)+(1/2)*((m0+m1)/m1)*(abs(x+1.0)-abs(x-1.0))
    return f
def dH_dt(H, t=0):
        return np.array([(-c1/c3)*f(H[1]-H[0]),
                     (-1/c3)*(f(H[1]-H[0])+H[2]),
                     c3*H[1],
                     (-c11/c3)*f(H[4]-H[3]),
                     (-1/c3)*(f(H[4]-H[3])+H[5])+(с0/c3)*(H[1]-H[4]),
                     c3*H[4],
                     (-c11/c3)*f(H[7]-H[6]),
                     (-1/c3)*(f(H[7]-H[6])+H[8])+(с0/c3)*(H[1]-H[7]),
                     c3*H[7]])
t = np.linspace(0, 500, 4000)
H0 = [0.5, 0.7, 0.9, 0.9, 0.9, 0.9, 1.05, 1.05, 1.05 ]
H, infodict = integrate.odeint(dH_dt, H0, t, full_output=True)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(H[1600:,0], H[1600:,1], H[1600:,2])
ax.plot(H[200:,3], H[200:,4], H[200:,5])
ax.plot(H[200:,6], H[200:,7], H[200:,8])
plt.show()

