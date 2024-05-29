from scipy.optimize import linprog

c = [-4, -2]

A = [[1, -2], [-3, -2], [9, 8]]
b = [4, -6, 72]

x0_bounds = (0, None)
x1_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# Виведення результатів
print("Оптимальне значення цільової функції:", -res.fun)
print("Оптимальні значення змінних:")
for i, x in enumerate(res.x, 1):
    print(f"x_{i}:", x)
