from scipy.optimize import linprog

# Coefficients of the objective function
c = [10, -7, -5]

# Coefficients of the inequality constraints
A = [
    [6, 15, 6],
    [14, 42, 16],
    [2, 8, 2]
]

# Right-hand side values of the inequality constraints
b = [9, 21, 4]

# Bounds for each variable
x0_bounds = (0, None)
x1_bounds = (0, None)
x2_bounds = (0, None)

# Solving the linear programming problem using the HiGHS method
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds, x2_bounds], method='highs')

# Printing the results
print("Результат:")
print(res.x)
print("Значення функції:")
print(res.fun)
