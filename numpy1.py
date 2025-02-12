import numpy as np

# 1. creating basic array  
array1 = np.array([1,2,3,4,5]);
print(array1);


#2 create a multi dimensional array

array2 = np.array([[1,2,3,4],
                  [5,6,7,8]]);
print(array2);

# 3.specifying data types of array
array3 = np.array([1,2,3,4],dtype=float);
print(array3);

#4. create array with range
array4 = np.arange(1,10,2.5);
print(array4);

#5 creating array with zero and ones
array5 = np.zeros((3,1));
print(array5);
array6 = np.ones((3,3));
print(array6);

#6 creating an identity matrix
array7 =  np.eye(3);
print(array7);

#7 creating a random array
array8 = np.random.rand(3,3);
print(array8);  