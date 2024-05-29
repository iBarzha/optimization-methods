import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd
from copy import deepcopy

def load_tsp(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    coords_start = False
    coords = []
    for line in lines:
        if line.startswith("NODE_COORD_SECTION"):
            coords_start = True
            continue
        if coords_start:
            if line.strip() == "EOF":
                break
            parts = line.split()
            coords.append((int(parts[1]), int(parts[2])))

    return np.array(coords)

coords = load_tsp('att48.tsp')

def nearest_neighbor(coords):
    num_nodes = len(coords)
    visited = [False] * num_nodes
    path = []
    current_node = 0
    path.append(current_node)
    visited[current_node] = True

    for _ in range(num_nodes - 1):
        next_node = None
        min_dist = float('inf')
        for j in range(num_nodes):
            if not visited[j]:
                dist = np.linalg.norm(coords[current_node] - coords[j])
                if dist < min_dist:
                    min_dist = dist
                    next_node = j
        current_node = next_node
        path.append(current_node)
        visited[current_node] = True

    return path

def calculate_path_length(coords, path):
    return sum(np.linalg.norm(coords[path[i]] - coords[path[(i + 1) % len(path)]]) for i in range(len(path)))

nn_path = nearest_neighbor(coords)
nn_path_length = calculate_path_length(coords, nn_path)
print(f"Метод найближчого сусіда: {nn_path_length}")

def simulated_annealing(coords, initial_temp, cooling_rate, stopping_temp):
    def swap_two_nodes(path):
        new_path = path.copy()
        i, j = random.sample(range(len(path)), 2)
        new_path[i], new_path[j] = new_path[j], new_path[i]
        return new_path

    def acceptance_probability(old_cost, new_cost, temperature):
        if new_cost < old_cost:
            return 1
        return np.exp((old_cost - new_cost) / temperature)

    current_path = list(range(len(coords)))
    current_cost = calculate_path_length(coords, current_path)
    temperature = initial_temp

    while temperature > stopping_temp:
        new_path = swap_two_nodes(current_path)
        new_cost = calculate_path_length(coords, new_path)

        if acceptance_probability(current_cost, new_cost, temperature) > random.random():
            current_path = new_path
            current_cost = new_cost

        temperature *= cooling_rate

    return current_path

initial_temp = 10000
cooling_rate = 0.995
stopping_temp = 1e-8
sa_path = simulated_annealing(coords, initial_temp, cooling_rate, stopping_temp)
sa_path_length = calculate_path_length(coords, sa_path)
print(f"Метод імітації відпалу: {sa_path_length}")

class AntColonyOptimization:
    def __init__(self, coords, num_ants, num_iterations, alpha, beta, evaporation_rate, pheromone_constant):
        self.coords = coords
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.pheromone_constant = pheromone_constant
        self.num_nodes = len(coords)
        self.pheromone = np.ones((self.num_nodes, self.num_nodes))
        self.distances = np.array([[np.linalg.norm(coords[i] - coords[j]) for j in range(self.num_nodes)] for i in range(self.num_nodes)])

    def run(self):
        best_path = None
        best_length = float('inf')

        for _ in range(self.num_iterations):
            all_paths = []
            all_lengths = []

            for _ in range(self.num_ants):
                path = [random.randint(0, self.num_nodes - 1)]
                visited = set(path)

                while len(path) < self.num_nodes:
                    current_node = path[-1]
                    probabilities = self.compute_probabilities(current_node, visited)
                    next_node = self.select_next_node(probabilities)
                    path.append(next_node)
                    visited.add(next_node)

                path_length = calculate_path_length(self.coords, path)
                all_paths.append(path)
                all_lengths.append(path_length)

                if path_length < best_length:
                    best_path = deepcopy(path)
                    best_length = path_length

            self.update_pheromones(all_paths, all_lengths)

        return best_path, best_length

    def compute_probabilities(self, current_node, visited):
        pheromone = self.pheromone[current_node]
        distance = self.distances[current_node]
        distance[distance == 0] = 1e-10  
        attractiveness = pheromone ** self.alpha * ((1 / distance) ** self.beta)

        for i in visited:
            attractiveness[i] = 0

        total_attractiveness = sum(attractiveness)
        return attractiveness / total_attractiveness if total_attractiveness > 0 else np.zeros_like(attractiveness)

    def select_next_node(self, probabilities):
        return np.random.choice(range(self.num_nodes), p=probabilities)

    def update_pheromones(self, all_paths, all_lengths):
        self.pheromone *= (1 - self.evaporation_rate)
        for path, length in zip(all_paths, all_lengths):
            for i in range(self.num_nodes):
                self.pheromone[path[i - 1], path[i]] += self.pheromone_constant / length
                self.pheromone[path[i], path[i - 1]] += self.pheromone_constant / length

num_ants = 10
num_iterations = 100
alpha = 1.0
beta = 2.0
evaporation_rate = 0.5
pheromone_constant = 100

aco = AntColonyOptimization(coords, num_ants, num_iterations, alpha, beta, evaporation_rate, pheromone_constant)
aco_path, aco_path_length = aco.run()
print(f"Мурашиний алгоритм: {aco_path_length}")

def plot_path(coords, path, title):
    path_coords = coords[path + [path[0]]]
    plt.figure(figsize=(10, 6))
    plt.plot(path_coords[:, 0], path_coords[:, 1], marker='o')
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

plot_path(coords, nn_path, "Метод найближчого сусіда")
plot_path(coords, sa_path, "Метод імітації відпалу")
plot_path(coords, aco_path, "Мурашиний алгоритм")

# Таблиця результатів
results = {
    "Метод": ["Метод найближчого сусіда", "Метод імітації відпалу", "Мурашиний алгоритм"],
    "Довжина отриманого шляху": [nn_path_length, sa_path_length, aco_path_length]
}

df = pd.DataFrame(results)
print(df)
