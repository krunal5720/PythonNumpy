# 14th february pratice file

import numpy as np  

# 1. accessing elements in numpy array
np1 = np.array([1,2,3,4,5]);
print(np1[1]); 
print(np1[2:4]); #slicing
print(np1[1:]); #slicing
print(np1[:4]); #slicing
print(np1[:]); #slicing
print(np1[-1]); #slicing

# 2. accessing elements in multi dimensional array

# 3. modifying elements using indexing
np3 = np.array([1,2,3,4,5]);
np3[1] = 10;
print(np3);

# 3.1 modifying multiple array using slicing
np3[1:3] = [1,2];
print(np3);

# 3.2 Modifying Elements Using Boolean Indexing
np3[np3>3] = 10;
print(np3);

#3.3 modifying elements using fancy indexing
np3[[2,4]] = [5,6];
print(np3);

# 3.4 applying operations on elements
np3 = np3 + 2 ;
print(np3);