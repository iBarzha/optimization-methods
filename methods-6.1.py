from scipy.optimize import linprog

profits = [[2, 6, 3, 4, 5],
           [4, 2, 2, 7, 3]]

mean_profit_A1 = sum(profits[0]) / len(profits[0])
mean_profit_A2 = sum(profits[1]) / len(profits[1])

c = [-mean_profit_A1, -mean_profit_A2]

A_eq = [[1, 1]]
b_eq = [1]

bounds = [(0, 1), (0, 1)]

res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds)

x1_optimal = res.x[0]
x2_optimal = res.x[1]

print("Оптимальні пропорції виробництва:")
print("Продукція A1:", x1_optimal)
print("Продукція A2:", x2_optimal)