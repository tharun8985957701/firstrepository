import numpy as np
import matplotlib.pyplot as plt

# Differential equation
def f(x, y):
    numerator = np.sin(x) + np.cos(y) + 2
    denominator = 2 * np.sin(x) + 2 * np.cos(y) + 3
    return numerator / denominator

# Initial condition
x0 = 0
y0 = 0

# Step size and range
h = 0.1
x_end = 10
n = int((x_end - x0) / h)

# Arrays to store values
x_vals = [x0]
y_vals = [y0]

# Euler method loop
x, y = x0, y0
for _ in range(n):
    y += h * f(x, y)
    x += h
    x_vals.append(x)
    y_vals.append(y)

# Plotting the result
plt.plot(x_vals, y_vals, label='Numerical Solution (Euler)', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Approximate Solution of dy/dx')
plt.legend()
plt.grid(True)
plt.show()
