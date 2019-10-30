from numpy import array
import numpy as np
import matplotlib.pyplot as plt
def  lagrange(x,i,xm):
    """Evaluates  the i-th  Lagrange  polynomial  at xbased on grid  dataxm"""
    n=len(xm)-1
    y=1.
    
    for j in  range(n+1):
        if i!=j:
            y*=(x-xm[j])/(xm[i]-xm[j])
    return y
def  interpolation(x,xm ,ym):
    n=len(xm)-1
    lagrpoly=array([lagrange(x,i,xm) for i in range(n+1)])
    y = np.dot(ym ,lagrpoly)
    return y

#newton interpolation

def NDD(x,y):
    n = len(x)
    #Construct table and load xy pairs in first columns
    A = zeros((n,n+1))
    A[:,0]= x[:]
    A[:,1]= y[:]
    #Fill in Divided differences
    for j in range(2,n+1):
        for i in range(j-1,n):
            A[i,j] = (A[i,j-1]-A[i-1,j-1]) / (A[i,0]-A[i-j+1,0])
    #Copy diagonal elements into array for returning
    p = zeros(n)
    for k in range(0,n):
        p[k] = A[k,k+1]
        return p
def poly(t,x,p):
    n = len(x)
    out = p[n-1]
    for i in range(n-2,-1,-1):
        out = out*(t-x[i]) + p[i]
        return out

