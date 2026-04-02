import numpy as np
arr4 = np.array([2,3,4,5,4,5,3,7,8,1,3,4,5,6,7,8,9,2,3,4,5,6,7,8])
new=arr4.reshape(4,2,-1)
print(new.shape)
print(new) 