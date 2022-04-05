import matplotlib.pyplot as plt
import numpy as np

c = plt.Circle((0,0),radius = 4, facecolor = "white", edgecolor = "Black")

ax = plt.gca()
ax.add_patch(c)

plt.plot(0,0, marker = ".", ms = 10, mfc = "green", mec = "green")
plt.plot(4,0, marker = ".", ms = 10, mfc = "green", mec = "green")

x=[0,4]
y=[0,0]
plt.plot(x,y,color = "black")

plt.annotate("C",(0.2,0.1))
plt.annotate("P",(4.2,0.1))
plt.axis("scaled")
plt.axis('off')
plt.show()
