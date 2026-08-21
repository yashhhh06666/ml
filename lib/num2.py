import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

# print(a+b) 
# print(b*2)
# print(np.sin(a))
# print(a.sum())

# # -------------

# print("Array a:", a)
# print("Array b:", b)

# arr_1d = np.array([1, 2, 3, ])
# arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
# print("1D Array:", arr_1d)
# print("2D Array:", arr_2d)

zero= np.zeros((2, 3))
one= np.ones((3, 2))
ranges= np.arange(0, 10, 2)

print("Zeros Array:\n", zero)
print("Ones Array:\n", one)
print("Range Array:", ranges)