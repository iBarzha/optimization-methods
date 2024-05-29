import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def f(x):
    return (x[0] - 2)**2 + x[1]**2

x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)
Z = f([X, Y])

plt.figure(figsize=(10, 6))
plt.contour(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar(label='f(x)')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Графік функції f(x) та лінії рівня')

res_nm = minimize(f, x0=[0, 0], method='Nelder-Mead')
x_min_nm, y_min_nm = res_nm.x[0], res_nm.x[1]
plt.plot(x_min_nm, y_min_nm, 'ro', label='Мінімум (Nelder-Mead)')

res_bfgs = minimize(f, x0=[0, 0], method='BFGS')
x_min_bfgs, y_min_bfgs = res_bfgs.x[0], res_bfgs.x[1]
plt.plot(x_min_bfgs, y_min_bfgs, 'bo', label='Мінімум (BFGS)')

print("Глобальний мінімум (Nelder-Mead):", res_nm.x)
print("Значення функції в точці мінімуму (Nelder-Mead):", res_nm.fun)
print("Глобальний мінімум (BFGS):", res_bfgs.x)
print("Значення функції в точці мінімуму (BFGS):", res_bfgs.fun)

plt.legend()
plt.show()
