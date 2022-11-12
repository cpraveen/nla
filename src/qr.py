import numpy as np

def mgs(A):
    m, n = A.shape
    V = A.copy()
    Q, R = np.empty((m,n)), np.zeros((n,n))
    for i in range(n):
        R[i,i] = np.linalg.norm(V[:,i])
        Q[:,i] = V[:,i] / R[i,i]
        for j in range(i+1,n):
            R[i,j] = Q[:,i].dot(V[:,j])
            V[:,j] = V[:,j] - R[i,j] * Q[:,i]
    return Q, R

# We need sign function with sign(0) = 1
def sign(x):
    if x >= 0.0:
        return 1.0
    else:
        return -1.0

def house(A,mode='full'):    
    # Algorithm 10.1
    R = A.copy()
    m, n = A.shape
    V = []
    for k in range(n):
        x = R[k:m,k]
        e1 = np.zeros_like(x); e1[0] = 1.0
        v = sign(x[0]) * np.linalg.norm(x) * e1 + x
        v = v / np.linalg.norm(v); V.append(v)
        for j in range(k,n):
            R[k:m,j] = R[k:m,j] - 2.0 * v * np.dot(v, R[k:m,j])
    
    # Algorithm 10.3
    # Compute Q as Q*I
    Q = np.empty((m,m))
    for i in range(m): # Compute i'th column of Q
        x = np.zeros(m)
        x[i] = 1.0
        for k in range(n-1,-1,-1):
            x[k:m] = x[k:m] - 2.0 * np.dot(V[k],x[k:m]) * V[k]
        Q[:,i] = x
        
    if mode == 'full':
        return Q, R
    elif mode == 'reduced':
        return Q[0:m,0:n], R[0:n,0:n]
    else:
        raise Exception("house: Unknown mode")
