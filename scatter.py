from matplotlib import pyplot as plt

x1 = [0.53, 0.40]
y1 = [0.73, 0.84]

x2 = [0.51, 0.42, 0.39, 0.32]
y2 = [0.76, 0.87, 0.89, 0.93]

plt.scatter(x1, y1, label='label 1')
plt.scatter(x2, y2, label='label 2')
plt.axis('square')
plt.axis([0, 1, 0, 1])
plt.grid()
plt.xlabel('x')
plt.ylabel('y)')
plt.legend(loc='lower right')
plt.show()