from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# DEFINE CONSTANTS
a = 1 # infection rate
b = 1/14 # recovery rate

# FUNCTION TO RETURN DERIVATIVES AT T
def f(y,t):
	S, I, _ = y # get previous values of S, I, R and store them in array y
	d0 = -a*S*I # derivative of S(t)
	d1 = a*S*I - b*I # derivative of I(t)
	d2 = b*I # derivative of R(t)

	return [d0, d1, d2]

# INITIAL VALUES OF EACH FUNCTION 
S_0 = 1
I_0 = 3.125/(10**6)
R_0 = 0
y_0 = [S_0,I_0,R_0]

t = np.linspace(start=1,stop=100,num=100)
y = odeint(f,y_0,t) 

S = y[:,0]
I = y[:,1]
R = y[:,2]

plt.figure()
plt.plot(t,S,"r",label="S(t)")
plt.plot(t,I,'b',label="I(t)")
plt.plot(t,R,'g',label="R(t)")
plt.legend()
plt.show()
