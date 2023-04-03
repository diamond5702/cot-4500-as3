# Question 1:
import numpy as np
np.set_printoptions(precision=7, suppress=True, linewidth=100)

def function(t: float , y: float):
  return t-(y**2)

def euler_method (t,y,tplus,n):
    #step function
    a=0
    b=2
    iterations = 10
    step_h = (b-a)/iterations
  
    for i in range (0, iterations):
        slope= function(t,y)
        yplus = y + (step_h*slope)
        y = yplus
        t = t + step_h
    return y

print(euler_method(0,1,1,10))    

# Question 2:

def function(t: float , y: float):
  return t-(y**2)

def rk_method(t,y,tplus,n):
    #Range
    a=0
    b=2
    #number of iterations
    iterations = 10
    #step function
    step_h = (b-a)/iterations
    #loop
    for i in range (0, iterations):
        k1= step_h * function(t,y)
        k2= step_h * function(t+ (step_h/2) , y + (k1/2) )
        k3= step_h * function(t+ (step_h/2) , y + (k2/2))
        k4= step_h * function(t+ (step_h) , y+ k3 )
        yplus =  1/6 * (k1 + 2*k2 + 2*k3 + k4) + y
        y= yplus
        t= t+ step_h
    return yplus

print(rk_method(0,1,1,10))


