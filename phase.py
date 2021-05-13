import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

с0 = 0.08
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
                     c3*H[4]])

t = np.linspace(1000, 2200, 5000)
H0 = [1, 1, 1, 1, 1, 1]
H, infodict = integrate.odeint(dH_dt, H0, t, full_output=True)
fig = plt.figure()
plt.plot(H[1600:,1], H[1600:,2])
plt.show()
