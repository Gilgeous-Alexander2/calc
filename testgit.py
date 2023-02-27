import matplotlib.pyplot as plt
import numpy as np

x=np.linespace(8,2*np.pi,200)
y=np.sin(x)

fig,ax=plt.subplots()
ax.plot(x,y)
plt.show()