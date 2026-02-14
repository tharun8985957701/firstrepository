import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x)
def f(x):
    return 0.1 - x + x**2 / (2)**2 - x**3 / (6) + x**4 / (24)**2
    # But since Python doesn’t allow factorial notation like (2!) directly,
    # we write the equivalent numeric form below.

# Corrected version:
def f(x):
    return 0.1 - x + x**2/4 - x**3/6 + x**4/576

# Derivative f'(x)
def fprime(x):
    return -1 + (2*x)/4 - (3*x**2)/6 + (4*x**3)/576

# Initial guess
x0 = 0.5
x_vals = [x0]

# Perform 4 iterations of Newton–Raphson
for i in range(4):
    x_next = x_vals[-1] - f(x_vals[-1]) / fprime(x_vals[-1])
    x_vals.append(x_next)

# Generate data for plotting
x = np.linspace(0, 0.5, 400)
y = f(x)

# Plot the function
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='f(x)', linewidth=2, color='orange')
plt.axhline(0, color='black', linestyle='--')  # x-axis

# Plot the iteration points
plt.scatter(x_vals, [f(xi) for xi in x_vals], color='red', label='Iterations')

# Label each iteration
for i, xi in enumerate(x_vals):
    plt.text(xi, f(xi) + 0.005, f"x{i}", fontsize=9, ha='center')

# Add labels and title
plt.title("Convergence of Newton–Raphson Method")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
