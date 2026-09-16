import numpy as np
import sys
python_list=list(range(1000))
numpy_array=np.arange(1000)
print("memory used by python list",sys.getsizeof(python_list))
print("memory used by numppy array",numpy_array.nbytes,"bytes")

