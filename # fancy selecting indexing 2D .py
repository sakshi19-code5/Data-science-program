#  fancy selecting indexing 2D
import numpy as np
arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
rows= np.array([0,1,2])
coloumns=np.array([2,1,0])
result=arr[rows,coloumns]
print("selected elements:",result)