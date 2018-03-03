import numpy as np
import math as ma
import matplotlib.pyplot as plt
#straight line y=2x-1

#x interval 10 and step =1
x_list=[0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5]
x = np.array(x_list)
y = 2*x-1
Y = np.sum(y)

#Parabola y=2x^2+3x-2
#x interval 10 and step 1
a_list=[0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5]
a = np.array(a_list)
b = 2*a**2+3*a-2
B = np.sum(b)

#complicated y=(2x+3)e^-0.2x
#x interval 10 and step 1
n_list=[0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5]
n = np.array(n_list)
m = (2*n+3)*ma.e**(-0.2*n)
M=np.sum(m)

print ("x from 0 to 10")
print (Y,"area y=2x-1"),(B,"area 2x^2+3x-2"),(M,"area (2x+3)e^-0.2x")
# We Know actual area under the curve by integration
# Which is 90,796.7,42.67
#k=percent diff 1 q=percent diff 2 j=percent diff 3
k=(0/((90+90)/2))
q=((796.7-795)/((796.7+795)/2))*100
j=((M-42.67)/((M+42.67)/2))*100

print ("percent diff:"),k,q,j
# if we have x step of 5
o_list=[2.5,7.5]
o = np.array(o_list)
O = (2*o+3)*ma.e**(-0.2*o)
P = np.sum(5*O)
p = (P-42.67)/((P+42.67)/2)*100

# if we have x step of 2
i_list=[1,3,5,7,9]
i = np.array(i_list)
I = (2*i+3)*ma.e**(-0.2*i)
U = np.sum(2*I)
u = (U-42.67)/((U+42.67)/2)*100

# if we have x step of 0.5
w_list=[0.25,0.75,1.25,1.75,2.25,2.75,3.25,3.75,4.25,4.75,5.25,5.75,6.25,6.75,7.25,7.75,8.25,8.75,9.25,9.75]
w = np.array(w_list)
R = (2*w+3)*ma.e**(-0.2*w)
W = np.sum(0.5*R)
r=(W-42.67)/((W+42.67)/2)*100

# if we have x step of 0.25
g_list=[0.125,0.375,0.625,0.875,1.125,1.375,1.625,1.875,2.125,2.375,2.625,2.875,3.125,3.375,3.625,3.875,4.125,4.375,4.625,4.875,5.125,5.375,5.625,5.875,6.125,6.375,6.625,6.875,7.125,7.375,7.625,7.875,8.125,8.375,8.625,8.875,9.125,9.375,9.625,9.875]
g = np.array(g_list)
G = (2*g+3)*ma.e**(-0.2*g)
h = np.sum(0.25*G)
H =(h-42.67)/((h+42.67)/2)*100

t=[0.25,0.5,1,2,5]
v=[H,r,j,u,p]
plt.scatter(t,v)
plt.show()
# So far we have step of 0.25,0.5,1,2,5 and H,r,j,u,p
