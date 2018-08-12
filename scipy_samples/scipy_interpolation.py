
from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 11)
y = x* np.sin(x) #np.exp(-x/3.0)
f = [interpolate.interp1d(x, y), interpolate.interp1d(x, y, kind='nearest')]

xnew = np.arange(0, 10.1, 0.1)
ynew = [f[0](xnew), f[1](xnew)]   # use interpolation function returned by `interp1d`

fig, ax = plt.subplots()
ax.plot(x, y, 'o', xnew, ynew[0], '-', xnew, ynew[1], '-')
fig.show()


x = np.arange(-5.01, 5.01, 0.5)
y = np.arange(-5.01, 5.01, 0.5)
xx, yy = np.meshgrid(x, y)
z = np.cos(np.sqrt(xx**2+yy**2))
f = interpolate.interp2d(x, y, z, kind='cubic')

import matplotlib.pyplot as plt
xnew = np.arange(-5.01, 5.01, 1e-2)
ynew = np.arange(-5.01, 5.01, 1e-2)
znew = f(xnew, ynew)
fig, ax = plt.subplots(3,1)
ax[0].plot(x, z[0, :], 'ro-', xnew, znew[0, :], 'b-')
ax[1].plot(x, z[5, :], 'ro-', xnew, znew[251, :], 'b-')
ax[2].plot(x, z[10, :], 'ro-', xnew, znew[501, :], 'b-')
fig.tight_layout()
fig.show()
