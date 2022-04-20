import matplotlib.pyplot as plt
import numpy as np

def cos(a):
    p = np.cos(a*np.pi/180)
    return p

def sin(a):
    p = np.sin(a*np.pi/180)
    return p

c = plt.Circle((0,0),radius = 4, facecolor = "white", edgecolor = "Black")

ax = plt.gca()
ax.add_patch(c)

plt.plot(0,0, marker = ".", ms = 10, mfc = "green", mec = "green")

plt.plot(4,0, marker = ".", ms = 10, mfc = "green", mec = "green")

plt.plot(4*cos(104), 4*sin(104), marker = ".", ms = 10, mfc = "green", mec = "green")

x1 = [0,4]
y1 = [0,0]
plt.plot(x1,y1, color = "black")

x2 = [0,4*cos(104)]
y2 = [0,4*sin(104)]
plt.plot(x2,y2, color = "black")

plt.annotate("P", (3.7,0.3))
plt.annotate("Q", (-1.5,3.9))
plt.annotate("C", (0.2,0.2))
plt.axis("scaled")

plt.axis('off')

plt.show()
