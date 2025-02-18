# 4. Array Manipulation

#==============================================================================
import numpy as np

#==============================================================================
#4.1 reshaping array using rshape() , flatten() and ravel()
np1 = np.array([1,2,3,4])

reshapArray  = np1.reshape(-1,4); # -1 means unknown dimension
print(reshapArray);

np2 = np.array([[1,2,3],
               [4,5,6]])
falttenarray = np2.ravel(); # ravel() is similar to flatten()
print(falttenarray);
faltenNewArray = np2.flatten(); # ravel() is similar to flatten()
print(faltenNewArray);


# ============================================================================
# 4.2 Adding and removing elements
np3 = np.array([4,5,6,7]);
a1 = np.append(np3,4);
a2 = np.append(np3,[4,5,6]); # append multiple elements


np4 = np.array([[1,2,3],
               [4,5,6]])
a2 = np.append(np4,[[7,8,9]],axis=0); # append row wise
a3 = np.append(np4,[[7],[8]],axis=1); # append column wise


# insert
newarray = np.insert(np3,1,100); # insert 100 at index 1
print(newarray);


# ===========================================================================
#4.3 Joining arrays
 
a = np.array([[1,2,3],
              [4,5,6]]);
b= np.array([[5,6,7]]);
r1 = np.concatenate((a,b),axis=0); # concatenate row wise
print(r1);