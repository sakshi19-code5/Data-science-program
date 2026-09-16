#missing values python
import numpy as np

data = np.genfromtxt(
    "ARRAY.csv",
    delimiter=",",
    skip_header=1
)

print("Original data:")
print(data)

for column in range(data.shape[1]):

    mean_value = np.nanmean(data[:, column])

    data[np.isnan(data[:, column]), column] = mean_value

print("\nCleaned data:")
print(data)
    