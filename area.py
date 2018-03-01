import numpy as np
import math as ma

#straight line y=2x-1
#x interval 10 and step =1
x_list=[0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5]
x = np.array(x_list)
y = 2*x-1

#Parabola y=2x^2+3x-2
#x interval 10 and step 1
a_list=[0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5]
a = np.array(a_list)
b = 2*a**2+3*a-2
###print (np.sum(x*y),np.sum(a*b))

#complicated y=(2x+3)e^-2x
#x interval 10 and step 1
n_list=[0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5]
n = np.array(n_list)
m = (2*n+3)*ma.e**(-2*n)


print ("x from 0 to 10")
print (np.sum(y),"area y=2x-1"),(np.sum(b),"area 2x^2+3x-2"),(np.sum(m),"area (2x+3)e^-2x")
# We Know actual area under the curve by integration
# Which is 90,796.7,-2.5*10^-8
#k=percent diff 1 q=percent diff 2 j=percent diff 3
k=(0/((90+90)/2))
q=((796.7-795)/((796.7+795)/2))*100
j=(1.835-(-2.5*10**(-8))/((1.835-2.5*10**(-8))/2))*100
print ("percent diff:"),k,q,j

# if we have x step of 0.5
w_list=[0.25,0.75,1.25,1.75,2.25,2.75,3.25,3.75,4.25,4.75,5.25,5.75,6.25,6.75,7.25,7.75,8.25,8.75,9.25,9.75]
w = np.array(w_list)
W = (2*w+3)*ma.e**(-2*w)
r=(np.sum(W)-(-2.5*10**(-8))/((np.sum(W)-2.5*10**(-8))/2)*100
