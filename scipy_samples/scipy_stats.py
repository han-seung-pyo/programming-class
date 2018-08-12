
import scipy.stats as sst
import numpy as np
import matplotlib.pyplot as plt

normdist = [sst.norm(0,1), sst.norm(1,0.5)]
x = np.linspace(-3,3,61)
pdf = [n.pdf(x) for n in normdist]
cdf = [n.cdf(x) for n in normdist]
rndsample = [n.rvs(10000) for n in normdist]

fig, ax = plt.subplots(3,1,figsize=(4,8))

ax[0].plot(x,pdf[0],x,pdf[1])
ax[0].set_title('normal pdf')

ax[1].plot(x,cdf[0],x,cdf[1])
ax[1].set_title('normal cdf')
ax[1].grid(True)

ax[2].hist(rndsample, bins=50)
ax[2].set_title('random sampling')

fig.tight_layout()
fig.show()





