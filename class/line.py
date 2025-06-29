'''This is a program of matplotlib'''
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 8, 16, 32]
z = [31,15,7,3,1]
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Line 1')
plt.plot(x, z, marker='s', linestyle='--', color='r', label='Line 2')
plt.title('Line Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()