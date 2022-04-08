import numpy as np

n=int(input())
while(n!=0):
    A=np.zeros(n,n)
    for i in range(n):
        A[i]=[float(k) for k in iput().split()]
    print(A)
    n=int(input())