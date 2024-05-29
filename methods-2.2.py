from scipy.optimize import linprog

# Coefficients of the objective function (for maximization, we minimize the negative)
c = [-4, -3]

# Coefficients of the inequality constraints
A = [
    [2, -1],
    [1, 2],
    [2, -0.1]
]

# Right-hand side values of the inequality constraints
b = [2, 3, 1]

# Bounds for each variable
x0_bounds = (0, None)
x1_bounds = (0, None)

# Solving the linear programming problem using the HiGHS method
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# Printing the results
print("Результат:")
print(res.x)
print("Значення функції:")
print(-res.fun)  # Negating to get the maximum value
