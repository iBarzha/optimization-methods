import numpy as np
from scipy.optimize import minimize

def objective(x):
    return 4*x[0]**2 + 4*x[1]**2 + 2*x[0] + x[1]

def constraint1(x):
    return 2*x[0] + 3*x[1] - 12

def constraint2(x):
    return 12 - (3*x[0] + 2*x[1])

def constraint3(x):
    return 8*x[0] + 5*x[1] - 14

x0 = [0, 0]

bnds = [(0, None), (0, None)]

con1 = {'type': 'ineq', 'fun': constraint1}
con2 = {'type': 'ineq', 'fun': constraint2}
con3 = {'type': 'ineq', 'fun': constraint3}
cons = [con1, con2, con3]

solution = minimize(objective, x0, method='SLSQP', bounds=bnds, constraints=cons)

print('Оптимальне значення:', solution.fun)
print('Оптимальні змінні:', solution.x)