import pulp

# Створюємо об'єкт задачі ЛП для максимізації
problem = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

# Оголошуємо змінні рішення
x1 = pulp.LpVariable('x1', lowBound=0)  # Кількість карамелі "Барбарис"
x2 = pulp.LpVariable('x2', lowBound=0)  # Кількість карамелі "Лапки"

# Додаємо обмеження
problem += 0.5*x1 + 0.6*x2 <= 800  # Витрати цукру
problem += 0.4*x1 + 0.3*x2 <= 600  # Витрати патоки
problem += 0.1*x1 + 0.1*x2 <= 120  # Витрати фруктового пюре

# Додаємо цільову функцію
problem += 112*x1 + 126*x2

# Розв'язуємо задачу
problem.solve()

# Виводимо результати
print("Кількість тонн карамелі 'Барбарис':", x1.value())
print("Кількість тонн карамелі 'Лапки':", x2.value())
print("Максимальний прибуток:", pulp.value(problem.objective))
