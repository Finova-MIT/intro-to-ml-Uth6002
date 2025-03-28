import matplotlib.pyplot as plt

a = [5, 5, 9, 2, 1]
b = [5, 7, 99, 11, 54]

plt.plot(a, b, color='b', marker='o', linestyle='-', linewidth=2, markersize=6)
plt.title("Simple Line Chart")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)
plt.show()

plt.scatter(a, b, color='r', marker='x', s=100) 
plt.title("Simple Scatter Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)
plt.show()