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

def nearest_neighbor(cities):
    n = len(cities)
    visited = [False] * n
    path = [0]
    visited[0] = True

    while len(path) < n:
        last = path[-1]
        next_city = np.argmin([np.linalg.norm(cities[last] - cities[j]) if not visited[j] else float('inf') for j in range(n)])
        path.append(next_city)
        visited[next_city] = True

    path.append(path[0])
    return path

nn_path = nearest_neighbor(cities)
nn_distance = sum(np.linalg.norm(cities[nn_path[i]] - cities[nn_path[i + 1]]) for i in range(len(nn_path) - 1))
print(f'Метод найближчого сусіда: {nn_distance}')
