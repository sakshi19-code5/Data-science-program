# load2 file
import numpy as np
data = np.loadtxt("ARRAY.csv",delimiter=",",skiprows=1)
print("Data:")
print(data)
print("Shape:", data.shape)
print("Number of rows:", data.shape[0])
print("Number of columns:", data.shape[1])