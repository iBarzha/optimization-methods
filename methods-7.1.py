import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

def f(x):
    return x**3 - 27*x + 5

x_values = np.linspace(-10, 10, 400)
y_values = f(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f(x) = x^3 - 27x + 5', color='blue')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Графік функції f(x)')
plt.grid(True)
plt.legend()

minimum = minimize_scalar(f, bounds=(-10, 10), method='bounded')
maximum = minimize_scalar(lambda x: -f(x), bounds=(-10, 10), method='bounded')

print("Мінімум функції: x =", minimum.x, ", f(x) =", minimum.fun)
print("Максимум функції: x =", maximum.x, ", f(x) =", -maximum.fun)

plt.scatter(minimum.x, minimum.fun, color='red', label='Мінімум')
plt.scatter(maximum.x, -maximum.fun, color='green', label='Максимум')
plt.legend()
plt.show()