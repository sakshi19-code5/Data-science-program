# load file
import numpy as np
data = np.loadtxt("C:\Users\laxma\OneDrive\Desktop\USER.CSV",delimiter=",",skiprows=1)

print(data)
print("Shape:", data.shape)
print("Number of rows:", data.shape[0])
print("Number of columns:", data.shape[1])