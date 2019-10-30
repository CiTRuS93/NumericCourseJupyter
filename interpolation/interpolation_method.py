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


