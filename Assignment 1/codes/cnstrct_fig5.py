import matplotlib.pyplot as plt
import numpy as np

r = 4
#radius of the circle, "r".

PSR = 82
SPQ = 73
PQS = 55
#INPUT values in degrees. Change them here to obtain the required configuration of the circle.

PCQ = 360 - 2*SPQ -2*PQS
PCR = 2*PSR
PCS = 2*PQS
#OUTPUT values. 

def cos(a):
    p = np.cos(a*np.pi/180)
    return p

def sin(a):
    p = np.sin(a*np.pi/180)
    return p

c = plt.Circle((0,0),radius = r, facecolor = "white", edgecolor = "Black")

ax = plt.gca()
ax.add_patch(c)

plt.plot(0,0, marker = ".", ms = 10, mfc = "green", mec = "green")

plt.plot(r,0, marker = ".", ms = 10, mfc = "green", mec = "green")

plt.plot(r*cos(PCQ), r*sin(PCQ), marker = ".", ms = 10, mfc = "green", mec = "green")

plt.plot(r*cos(PCR), r*sin(PCR), marker = ".", ms = 10, mfc = "green", mec = "green")

plt.plot(r*cos(PCS), -r*sin(PCS), marker = ".", ms = 10, mfc = "green", mec = "green")

x1 = [0,r]
y1 = [0,0]
plt.plot(x1,y1, color = "black")

x2 = [0,r*cos(PCQ)]
y2 = [0,r*sin(PCQ)]
plt.plot(x2,y2, color = "black")

x3 = [0,r*cos(PCR)]
y3 = [0,r*sin(PCR)]
plt.plot(x3,y3, color = "black")

x4 = [0,r*cos(PCS)]
y4 = [0,-r*sin(PCS)]
plt.plot(x4,y4, color = "black")

x5 = [r*cos(PCQ),r*cos(PCR)]
y5 = [r*sin(PCQ),r*sin(PCR)]
plt.plot(x5,y5, color = "black")

x6 = [r*cos(PCS),r*cos(PCR)]
y6 = [-r*sin(PCS),r*sin(PCR)]
plt.plot(x6,y6, color = "black")

x7 = [r*cos(PCS),r]
y7 = [-r*sin(PCS),0]
plt.plot(x7,y7, color = "black")

x8 = [r*cos(PCQ),r]
y8 = [r*sin(PCQ),0]
plt.plot(x8,y8, color = "black")



plt.annotate("P", (r + (r/20), r/20))
plt.annotate("Q", ((r*cos(PCQ) + (r/40)), (r*sin(PCQ) + (r/20))))
plt.annotate("R", ((r*cos(PCR) - (r/16)), (r*sin(PCR) + (r/20))))
plt.annotate("S", ((r*cos(PCS) - (r/20)), (-r*sin(PCS) - (r/10))))
plt.annotate("C", (r/25,r/25))
plt.axis("scaled")

plt.axis('off')

plt.show()
