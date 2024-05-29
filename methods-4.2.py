import random
import numpy as np

def load_tsp(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    cities = []
    for line in lines:
        if line.startswith('NODE_COORD_SECTION'):
            break
    node_section = False
    for line in lines:
        if node_section:
            if line.startswith('EOF'):
                break
            parts = line.split()
            cities.append((float(parts[1]), float(parts[2])))
        if line.startswith('NODE_COORD_SECTION'):
            node_section = True
    return np.array(cities)

cities = load_tsp('att48.tsp')

def simulated_annealing(cities, initial_temp, cooling_rate, stopping_temp):
    def calculate_distance(path):
        return sum(np.linalg.norm(cities[path[i]] - cities[path[i + 1]]) for i in range(len(path) - 1))

    def swap_two_cities(path):
        new_path = path.copy()
        i, j = random.sample(range(len(path) - 1), 2)
        new_path[i], new_path[j] = new_path[j], new_path[i]
        return new_path

    n = len(cities)
    current_path = list(range(n)) + [0]
    current_distance = calculate_distance(current_path)
    best_path, best_distance = current_path, current_distance

    temp = initial_temp
    while temp > stopping_temp:
        new_path = swap_two_cities(current_path)
        new_distance = calculate_distance(new_path)

        if new_distance < current_distance or random.random() < np.exp((current_distance - new_distance) / temp):
            current_path, current_distance = new_path, new_distance
            if new_distance < best_distance:
                best_path, best_distance = new_path, new_distance

        temp *= cooling_rate

    return best_path, best_distance

sa_path, sa_distance = simulated_annealing(cities, initial_temp=10000, cooling_rate=0.995, stopping_temp=1)
print(f'Метод імітації відпалу: {sa_distance}')
