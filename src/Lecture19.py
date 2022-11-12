from numpy import linspace,empty,exp,sin,arcsin,column_stack
from numpy.linalg import lstsq,norm,solve,qr,svd
from qr import mgs,house

m, n = 100, 15
t = linspace(0,1,m)
A = empty((m,n))
for i in range(n):
    A[:,i] = t**i
b = exp(sin(4*t))
b = b/2006.787453080206

x,_,_,s = lstsq(A,b,rcond=None); y = A @ x
kappa = s.max() / s.min()
print('kappa = %10.4e' % kappa)
theta = arcsin(norm(b-y)/norm(b))
print('theta = %10.4e' % theta)
eta   = s.max() * norm(x) / norm(y)
print('eta   = %10.4e' % eta)

# numpy.linalg.qr
Q,R = qr(A)
x = solve(R, Q.T @ b)
print('\nnumpy.linalg.qr')
print('x_15, x_15-1 =',x[-1], x[-1]-1)

# numpy.linalg.qr augmented
Q2,R2 = qr(column_stack((A,b)))
Qb = R2[0:n,n]   # Last column of R2
R  = R2[0:n,0:n]
x = solve(R,Qb)
print('\nnumpy.linalg.qr augmented')
print('x_15, x_15-1 =',x[-1], x[-1]-1)

# Householder triangularization
Q,R = house(A,mode='reduced')
x = solve(R, Q.T @ b)
print('\nHouseholder triangularization')
print('x_15, x_15-1 =',x[-1], x[-1]-1)

# Modified GS
Q, R = mgs(A)
x = solve(R, Q.T@b)
print('\nModified GS')
print('x_15, x_15-1 =',x[-1], x[-1]-1)

# Modified GS, augmented
Q2,R2 = mgs(column_stack((A,b)))
Qb = R2[0:n,n]   # Last column of R2
R  = R2[0:n,0:n]
x = solve(R,Qb)
print('\nModified GS augmented')
print('x_15, x_15-1 =',x[-1], x[-1]-1)

# Normal equation
x = solve(A.T@A, A.T@b)
print('\nNormal equations')
print('x_15, x_15-1 =',x[-1], x[-1]-1)

# SVD
U,S,VT = svd(A,full_matrices=False) # reduced SVD
x = VT.T @ ((U.T@b)/S)
print('\nSVD')
print('x_15,x_15-1=',x[-1], x[-1]-1)
