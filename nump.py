import numpy as np

# a= np.arange(15).reshape(3,5)

a= np.arange(1,5).reshape(2,2)

b=np.arange(7,11).reshape(2,2)

print(a)
print(b)
print("-"*50)
print("Scaler Multiplication")
print(a*b)


print("-"*50)

print("Matrix Multiplication")
print(a@b)