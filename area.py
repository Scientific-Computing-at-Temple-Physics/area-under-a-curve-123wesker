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
