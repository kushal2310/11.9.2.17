import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("gen_values.txt")
x_values = data[:,0]
y_values = data[:,1]
#print(y_values) Used while debugging
#print(x_values) Used while debugging
plt.stem(x_values,y_values)
plt.scatter(29, 245, color = 'green')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid(True)
plt.savefig('y(t)_vs_t.png')
