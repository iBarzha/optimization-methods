from scipy.optimize import linprog

c_b = [3, 8]
A_b = [[-5, -3], [2, -3], [-1, -2]]
b_b = [-10, 6, -4]
bounds_b = [(0, None), (0, None)]

res_b = linprog(c_b, A_ub=A_b, b_ub=b_b, bounds=bounds_b, method='highs')
print('Пряма задача (б):')
print('Оптимальне значення цільової функції:', res_b.fun)
print('Оптимальні значення змінних:', res_b.x)

c_b_dual = [-10, -6, -4]
A_b_dual = [[5, 2, 1], [3, -3, 2]]
b_b_dual = [3, 8]
bounds_b_dual = [(0, None), (0, None), (0, None)]

res_b_dual = linprog(c_b_dual, A_ub=A_b_dual, b_ub=b_b_dual, bounds=bounds_b_dual, method='highs')
print('\nДвоїста задача (б):')
print('Оптимальне значення цільової функції:', -res_b_dual.fun)
print('Оптимальні значення змінних:', res_b_dual.x)
