import matplotlib.pyplot as plt
import numpy as np

c = plt.Circle((0,0),radius = 4, facecolor = "white", edgecolor = "Black")

ax = plt.gca()
ax.add_patch(c)

plt.axis("scaled")
plt.show()
