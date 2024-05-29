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

class AntColony:
    def __init__(self, cities, n_ants, n_best, n_iterations, decay, alpha=1, beta=1):
        self.cities = cities
        self.distances = self.calculate_distances(cities)
        self.pheromone = np.ones(self.distances.shape) / len(cities)
        self.all_inds = range(len(cities))
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def calculate_distances(self, cities):
        distances = np.zeros((len(cities), len(cities)))
        for i, city1 in enumerate(cities):
            for j, city2 in enumerate(cities):
                distances[i, j] = np.linalg.norm(city1 - city2)
        # Додаємо маленьке число до відстаней, щоб уникнути ділення на нуль
        distances[distances == 0] = np.inf
        return distances

    def run(self):
        shortest_path = None
        all_time_shortest_path = ("placeholder", np.inf)
        for i in range(self.n_iterations):
            all_paths = self.gen_all_paths()
            self.spread_pheronome(all_paths, self.n_best, shortest_path=shortest_path)
            shortest_path = min(all_paths, key=lambda x: x[1])
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path
            self.pheromone *= self.decay
        return all_time_shortest_path

    def gen_path_dist(self, path):
        total_dist = 0
        for i in range(len(path)):
            total_dist += self.distances[path[i-1]][path[i]]
        return total_dist

    def gen_all_paths(self):
        all_paths = []
        for i in range(self.n_ants):
            path = self.gen_path(0)
            all_paths.append((path, self.gen_path_dist(path)))
        return all_paths

    def gen_path(self, start):
        path = []
        visited = set()
        visited.add(start)
        prev = start
        for i in range(len(self.cities) - 1):
            move = self.pick_move(self.pheromone[prev], self.distances[prev], visited)
            path.append(move)
            prev = move
            visited.add(move)
        path.append(start)
        return path

    def pick_move(self, pheromone, dist, visited):
        pheromone = np.copy(pheromone)
        pheromone[list(visited)] = 0

        row = pheromone ** self.alpha * ((1.0 / dist) ** self.beta)
        # Обробляємо можливі NaN значення
        row = np.nan_to_num(row)
        norm_row = row / row.sum()
        move = np.random.choice(self.all_inds, 1, p=norm_row)[0]
        return move

    def spread_pheronome(self, all_paths, n_best, shortest_path):
        sorted_paths = sorted(all_paths, key=lambda x: x[1])
        for path, dist in sorted_paths[:n_best]:
            for move in path:
                self.pheromone[move] += 1.0 / self.distances[move]

colony = AntColony(cities, 100, 20, 100, 0.95, alpha=1, beta=2)
shortest_path, ac_distance = colony.run()
print(f'Мурашиний алгоритм: {ac_distance}')