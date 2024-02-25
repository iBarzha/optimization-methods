import pulp

# Створюємо об'єкт задачі ЛП для максимізації
problem = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

# Оголошуємо змінні рішення
x1 = pulp.LpVariable('x1', lowBound=0, cat='Integer')  # Кількість мобільних телефонів
x2 = pulp.LpVariable('x2', lowBound=0, cat='Integer')  # Кількість телевізорів

# Додаємо обмеження
problem += 4*x1 + 6*x2 <= 120  # Виробнича потужність ділянки A
problem += 2*x1 + 6*x2 <= 72   # Виробнича потужність ділянки B
problem += x2 <= 10            # Виробнича потужність ділянки C

# Додаємо цільову функцію
problem += 120*x1 + 460*x2

# Розв'язуємо задачу
problem.solve()

# Виводимо результати
print("Кількість мобільних телефонів: {}".format(x1.value()))
print("Кількість телевізорів: {}".format(x2.value()))
print("Максимальний прибуток: ${}".format(pulp.value(problem.objective)))
