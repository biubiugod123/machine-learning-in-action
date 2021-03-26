from numpy import *

a = mat(random.rand(4,4))
b = a.I
myeye = a * b
print(myeye)
print(eye(4))
