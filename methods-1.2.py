import pulp

# Створюємо об'єкт задачі ЛП для мінімізації
problem = pulp.LpProblem("Minimize_Cost", pulp.LpMinimize)

# Оголошуємо змінні рішення
x1 = pulp.LpVariable('x1', lowBound=0, cat='Integer')  # Кількість "КамАЗів"
x2 = pulp.LpVariable('x2', lowBound=0, cat='Integer')  # Кількість "КрАЗів"

# Додаємо обмеження
problem += 5*x1 + 8*x2 >= 160  # Вантажопідйомність
problem += 1.5*x1 + 2*x2 <= 150  # Витрати мастильних матеріалів
problem += 40*x1 + 50*x2 <= 1000  # Витрати палива

# Додаємо цільову функцію
problem += 10*x1 + 15*x2

# Розв'язуємо задачу
problem.solve()

# Виводимо результати
print("Кількість 'КамАЗів': {}".format(x1.value()))
print("Кількість 'КрАЗів': {}".format(x2.value()))
print("Мінімальні експлуатаційні витрати: {} у.г.о.".format(pulp.value(problem.objective)))

