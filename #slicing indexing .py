#slicing indexing
import numpy as np
arr=np.array([10,20,30,40,50,60,70])
print("original aaray:",arr)
print("elements from index 1 t0 4:",arr[1:5])
print("first 3 element:",arr[:3])
print("last 3 element:",arr[-3:])
print("every second element:",arr[::2])