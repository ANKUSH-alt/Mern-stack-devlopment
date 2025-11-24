import app as np
import time
import sys

b=range(10000)
print(sys.getsizeof(100)*len(b))
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)
print("Sum =", np.sum(arr))
import numpy as np
a = np.array([1, 2, 3])
b = np.array([2,3,4])

print(a,b.shape)
c=np.arange(9)
print(c.size*c.itemsize)