import matplotlib.pyplot as plt
import numpy as np

def f(x):
    y = 3*x/4 - 7 + 27/x
    return y
    
def g(x):
    y = 3*x/2 - 7
    return y
    
xaxisx = [-8,8]
xaxisy = [0,0]

yaxisx = [0,0]
yaxisy = [-35,35]

xpoints = [6,-6]
ypoints = [2,-16]
    
x1list = np.linspace(1,8,num = 500)
y1list = f(x1list)

x2list = np.linspace(-8,-1,num = 500)
y2list = f(x2list)

xlist = np.linspace(-8,8,num = 500)
ylist = g(xlist)

plt.plot(xaxisx, xaxisy, color = "k")
plt.plot(yaxisx, yaxisy, color = "k")
plt.plot(x1list, y1list, color = "r", label = "$y = 3x/4 - 7 + 27/x$")
plt.plot(x2list, y2list, color = "r")
plt.plot(xlist, ylist, color = "b", label = "$y = 3x/2 - 7$")
plt.scatter(xpoints, ypoints, s = 25, color = "black")

plt.text(5.5,3.5,"(6,2)")
plt.text(-7,-14,"(-6,-16)")

plt.legend(loc = "best")
plt.show()
