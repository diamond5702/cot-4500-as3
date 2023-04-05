# Question 1:
import numpy as np
np.set_printoptions(precision=7, suppress=True, linewidth=100)


def function(t: float , y: float):
  return t-(y**2)

def euler_method (t,y,tplus,n):
    #Range
    a=0
    b=2
    #number of iterations
    iterations = 10
    #step function
    step_h = (b-a)/iterations
    
    #loop
    for i in range (0, iterations):
        slope= function(t,y)
        yplus = y + (step_h*slope)
        y = yplus
        t = t + step_h
    return y


print("%.5f\n" % euler_method(0,1,1,10))


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
    #loo
    for i in range (0, iterations):
        k1= step_h * function(t,y)
        k2= step_h * function(t+ (step_h/2) , y + (k1/2) )
        k3= step_h * function(t+ (step_h/2) , y + (k2/2))
        k4= step_h * function(t+ (step_h) , y+ k3 )
        yplus =  1/6 * (k1 + 2*k2 + 2*k3 + k4) + y
        y= yplus
        t= t+ step_h
    return yplus

print("%.5f\n" % rk_method(0,1,1,10))

#Question 3:

def gauss(A,b):
    n = len(b)
   
    Ab = np.concatenate((A, b.reshape(3,1)), axis=1)
    # Elimination 
    for i in range(3):
        # Find the pivot row
        pivot_row = i
        for j in range(i+1, 3):
            if abs(Ab[j,i]) > abs(Ab[pivot_row,i]):
                pivot_row = j
        # Swap rows
        Ab[[i,pivot_row],:] = Ab[[pivot_row,i],:]
    
        for j in range(i+1, 3):
            factor = Ab[j,i]/Ab[i,i]
            Ab[j,i:4] = Ab[j,i:4] - factor * Ab[i,i:4]

    # Back substitution
    x = np.zeros(3)
    for i in range(2, -1, -1):
        x[i] = Ab[i,3]
        for j in range(i+1, 3):
            x[i] = x[i] - Ab[i,j] * x[j]
        x[i] = x[i] / Ab[i,i]

    print(x,"\n")
A= np.array([[2,-1,1],
             [1,3,1],
             [-1,5,4]],dtype=np.double)
b= np.array([[6,0,-3]],dtype=np.double)    

gauss(A,b)

#Question 4:

#a
matrix = np.array([[1 ,1, 0, 3],
                  [2, 1, -1, 1],
                  [3, -1, -1, 2],
                  [-1, 2, 3, -1]])

determinant= np.linalg.det(matrix)

print(determinant,"\n")

#b
matrix = np.array([[1 ,1, 0, 3],
                  [2, 1, -1, 1],
                  [3, -1, -1, 2],
                  [-1, 2, 3, -1]])

# Augment the matrix 
Ab = np.concatenate((matrix, np.zeros((4, 1))), axis=1)

# Forward elimination
for i in range(4):
    # Find the pivot row
    pivot_row = i
    for j in range(i+1, 4):
        if abs(Ab[j,i]) > abs(Ab[pivot_row,i]):
            pivot_row = j
    # Swap the rows
    Ab[[i,pivot_row],:] = Ab[[pivot_row,i],:]
    # Compute the multipliers 
    for j in range(i+1, 4):
        m = Ab[j,i] / Ab[i,i]
        Ab[j,i] = m
        Ab[j,i+1:5] = Ab[j,i+1:5] - m * Ab[i,i+1:5]

#L matrix
Lmatrix = np.tril(Ab[:, 0:4], k=-1)+ np.eye(4) 
print(Lmatrix,"\n")

#c
matrix = np.array([[1 ,1, 0, 3],
                  [2, 1, -1, 1],
                  [3, -1, -1, 2],
                  [-1, 2, 3, -1]])

# Augment the matrix 
Ab = np.concatenate((matrix, np.zeros((4, 1))), axis=1)
#elimination
for i in range(Ab.shape[0]):
    pivot = Ab[i,i]
    for j in range(i+1, Ab.shape[0]):
        factor = Ab[j,i] / pivot
        Ab[j,:] -= factor * Ab[i,:]
Umatrix = np.triu(Ab[:, 0:-1])

print(Umatrix,"\n")


#Question 5

def diagdom(matrix):
    n=matrix.shape[0]
    matrix = np.array([[9,0,5,2,1],
                  [3,9,1,2,1],
                  [0,1,7,2,3],
                  [4,2,3,12,2],
                   [3,2,4,0,8]])
    for i in range(n):
        if abs(A[i,i]) < np.sum(np.abs(A[i,:])) - abs(A[i,i]):
            return False
    return True
print(diagdom(matrix),"\n")


#Question 6

def pd(matrix):
    matrix=np.array([[2,2,1],
                     [2,3,0],
                     [1,0,2]])
    if np.all(np.linalg.eigvals(matrix)>0):
        return True
    else:
        return False
print(pd(matrix),"\n\n")
