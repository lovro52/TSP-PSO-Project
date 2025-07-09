import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import radians, sin, cos, sqrt, atan2
import random

# Učitavanje koordinata iz CSV datoteke
df = pd.read_csv("data/coords.csv")
coords_list = list(zip(df['Latitude'], df['Longitude']))

# Haversine formula za udaljenost između dvije točke
def haversine(coord1, coord2):
    R = 6371  # Zemljin radijus u km
    lat1, lon1 = map(radians, coord1)
    lat2, lon2 = map(radians, coord2)
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))

# Matrica udaljenosti
def create_distance_matrix(coords):
    size = len(coords)
    matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            if i != j:
                matrix[i][j] = haversine(coords[i], coords[j])
    return matrix

# Funkcija cilja – ukupna duljina rute
def fitness(route, distance_matrix):
    return sum(distance_matrix[route[i], route[(i + 1) % len(route)]] for i in range(len(route)))

# Klasa čestice za PSO
class Particle:
    def __init__(self, num_cities):
        self.position = np.random.permutation(num_cities)
        self.best_position = self.position.copy()
        self.best_fitness = float('inf')

    def update(self, global_best, distance_matrix):
        new_position = self.position.copy()
        for _ in range(2):  # Swap mutacija
            i, j = random.sample(range(len(new_position)), 2)
            new_position[i], new_position[j] = new_position[j], new_position[i]
        if fitness(new_position, distance_matrix) < fitness(self.position, distance_matrix):
            self.position = new_position
        if fitness(self.position, distance_matrix) < self.best_fitness:
            self.best_position = self.position.copy()
            self.best_fitness = fitness(self.position, distance_matrix)

# PSO algoritam
def pso_tsp(coords, n_particles=50, n_iterations=500):
    distance_matrix = create_distance_matrix(coords)
    particles = [Particle(len(coords)) for _ in range(n_particles)]
    global_best = min(particles, key=lambda p: fitness(p.position, distance_matrix))
    best_route = global_best.position
    best_distance = fitness(best_route, distance_matrix)

    for _ in range(n_iterations):
        for particle in particles:
            particle.update(best_route, distance_matrix)
        current_global = min(particles, key=lambda p: fitness(p.position, distance_matrix))
        if fitness(current_global.position, distance_matrix) < best_distance:
            best_route = current_global.position
            best_distance = fitness(best_route, distance_matrix)

    return best_route, best_distance

# Vizualizacija najbolje rute
def plot_route(route, coords):
    cities = [coords[i] for i in route] + [coords[route[0]]]
    lats, lons = zip(*cities)
    plt.figure(figsize=(10, 6))
    plt.plot(lons, lats, 'o-', markersize=5)
    for i, (lat, lon) in enumerate(cities):
        plt.text(lon, lat, str(i), fontsize=8)
    plt.title("Najbolja pronađena ruta (PSO)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.savefig("results/route_plot.png")
    plt.show()

# Pokretanje
if __name__ == "__main__":
    route, distance = pso_tsp(coords_list)
    print(f"Najbolja udaljenost: {distance:.2f} km")
    with open("results/best_distance.txt", "w") as f:
        f.write(f"Najbolja udaljenost: {distance:.2f} km\nRuta: {route.tolist()}")
    plot_route(route, coords_list)

    print("\nRedoslijed obilaska gradova:")
    for i in route:
        city_name = df.iloc[i]['City']
        print(f"- {city_name}")
