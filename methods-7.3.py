import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

def f(x):
    return (x**2 - 2*x) * np.log(x) - (3/2) * x**2 + 4*x

interval = (2, 4)

# Пошук глобального мінімуму
res = minimize_scalar(f, bounds=interval, method='bounded')

print("Глобальний мінімум:", res.x)
print("Значення функції в точці мінімуму:", res.fun)

x_values = np.linspace(1, 5, 400)
y_values = f(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f(x)')
plt.scatter(res.x, res.fun, color='red', label='Мінімум')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Графік функції f(x)')
plt.grid(True)
plt.legend()
plt.show()