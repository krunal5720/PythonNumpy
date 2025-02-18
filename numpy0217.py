# =========================================================================
# Mathematical Operations
#=========================================================================

# 1. basic arithmatic operations
import numpy as np
a = np.array([1,2,3,4]);
b = np.array([5,6,7,8]);
result1 = a + b; # add
result2  = a - b; # subtract    
result3 = a * b; # multiply
result4 = a / b; # divide


#2. universal functions
r1= np.add(a,b); # add
r2 = np.subtract(a,b); # subtract
r3 = np.multiply(a,b); # multiply   
r4 = np.divide(a,b); # divide

# 3. other mathematical operations
r5 = np.exp(a); # exponential
r6 = np.log(a); # logarithm
r7 = np.log10(a); # logarithm base 10

# 4.power and root functions
r8 =np.sqrt(a); # square root
r9 = np.power(a,2); # power

# 5. Absolute value and rounding functions
r10 = np.abs(a); # absolute value alsway positive value 
r11= np.round([1.2,1.5,1.6,2.5,2.7,2.9]); # round of the values

# 6 trigonometric functions
r12 = np.sin(a); # sine
r13 = np.cos(a); # cosine
r14 = np.tan(a); # tangent
r15 = np.arcsin(a); # arcsine
r16 = np.arccos(a); # arccosine
r17 = np.arctan(a); # arctangent

#7 statistical functions
r18 = np.mean(a); # mean
r19 = np.median(a); # median
r20 = np.std(a); # standard deviation
r21 = np.var(a); # variance
r22 = np.sum(a); # sum
r23 = np.prod(a); # product
r24 = np.cumsum(a); # cumulative sum
r25 = np.cumprod(a); # cumulative product

