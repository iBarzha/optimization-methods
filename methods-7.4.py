import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def f(X):
    x1, x2 = X
    return 7 * x1**2 + 2 * x1 * x2 + 5 * x2**2 + x1 - 10 * x2

x1 = np.linspace(-10, 10, 400)
x2 = np.linspace(-10, 10, 400)
X1, X2 = np.meshgrid(x1, x2)
Z = f([X1, X2])

plt.figure(figsize=(10, 6))
plt.contour(X1, X2, Z, levels=20, cmap='viridis')
plt.colorbar(label='f(X)')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Графік функції f(X) та лінії рівня')

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
