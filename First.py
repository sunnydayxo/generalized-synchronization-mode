import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
                     c3*H[1]])
t = np.linspace(0, 500, 4000)
H0 = [0.5, 0.7, 0.9 ]
H, infodict = integrate.odeint(dH_dt, H0, t, full_output=True)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(H[:1500,0], H[:1500,1], H[:1500,2])
plt.show()
