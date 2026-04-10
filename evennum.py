import numpy as np

arr = np.arange(1, 21)
even = arr[arr % 2 == 0]
print(even)