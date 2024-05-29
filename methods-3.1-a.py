from scipy.optimize import linprog

c_a = [-4, -2]
A_a = [[1, -2], [-3, -2], [9, 8]]
b_a = [4, -6, 72]
bounds_a = [(0, None), (0, None)]

res_a = linprog(c_a, A_ub=A_a, b_ub=b_a, bounds=bounds_a, method='highs')
print('Пряма задача (а):')
print('Оптимальне значення цільової функції:', -res_a.fun)
print('Оптимальні значення змінних:', res_a.x)

c_a_dual = [4, 6, 72]
A_a_dual = [[1, -3, 9], [2, -2, 1]]
b_a_dual = [4, 6]
bounds_a_dual = [(0, None), (0, None), (0, None)]

res_a_dual = linprog(c_a_dual, A_ub=A_a_dual, b_ub=b_a_dual, bounds=bounds_a_dual, method='highs')
print('\nДвоїста задача (а):')
print('Оптимальне значення цільової функції:', res_a_dual.fun)
print('Оптимальні значення змінних:', res_a_dual.x)
