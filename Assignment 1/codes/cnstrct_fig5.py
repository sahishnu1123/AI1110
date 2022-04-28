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

def u_vec(theta):
    v = np.array([cos(theta),sin(theta)])
    return v
    
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

def plot(x):
    plt.plot(x[0,:], x[1,:], 'k')
    return 0

C = np.array([0,0])
P = r*u_vec(0)
Q = r*u_vec(PCQ)
R = r*u_vec(PCR)
S = r*u_vec(360 - PCS)

c = plt.Circle((C),radius = r, facecolor = "white", edgecolor = "Black")

ax = plt.gca()
ax.add_patch(c)

x_PC = line_gen(P,C)
x_QC = line_gen(Q,C)
x_RC = line_gen(R,C)
x_SC = line_gen(S,C)
x_PQ = line_gen(P,Q)
x_QR = line_gen(Q,R)
x_RS = line_gen(R,S)
x_SP = line_gen(S,P)

plot(x_PC)
plot(x_QC)
plot(x_RC)
plot(x_SC)
plot(x_PQ)
plot(x_QR)
plot(x_RS)
plot(x_SP)


coords = np.vstack((P,Q,R,S,C)).T
plt.scatter(coords[0,:], coords[1,:])
vert_labels = ['P','Q','R','S','C']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (coords[0,i], coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-8,6), # distance from text to points (x,y)
                 ha='left') # horizontal alignment can be left, right or center




plt.axis("scaled")
plt.axis('off')

plt.show()
