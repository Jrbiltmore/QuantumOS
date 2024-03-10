# GeneticAlgorithm.py

import random
from typing import List, Tuple

class GeneticAlgorithm:
    def __init__(self, population_size: int, chromosome_length: int, generations: int, mutation_rate: float):
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.generations = generations
        self.mutation_rate = mutation_rate

    def initialize_population(self) -> List[List[int]]:
        return [[random.randint(0, 1) for _ in range(self.chromosome_length)] for _ in range(self.population_size)]

    def fitness_function(self, chromosome: List[int]) -> int:
        return sum(chromosome)

    def select_parents(self, population: List[List[int]]) -> Tuple[List[int], List[int]]:
        fitness_values = [self.fitness_function(chromosome) for chromosome in population]
        total_fitness = sum(fitness_values)
        # Apply roulette wheel selection with fitness-proportional probabilities
        parent1 = random.choices(population, weights=fitness_values, k=1)[0]
        parent2 = random.choices(population, weights=fitness_values, k=1)[0]
        return parent1, parent2

    def crossover(self, parent1: List[int], parent2: List[int]) -> Tuple[List[int], List[int]]:
        # Randomly select crossover point
        crossover_point = random.randint(1, len(parent1) - 1)
        # Perform one-point crossover
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    def mutate(self, chromosome: List[int]) -> List[int]:
        # Apply bit-flip mutation with given mutation rate
        return [1 - gene if random.random() < self.mutation_rate else gene for gene in chromosome]

    def evolve_population(self, population: List[List[int]]) -> List[List[int]]:
        new_population = []
        # Create new population through selection, crossover, and mutation
        for _ in range(self.population_size // 2):
            parent1, parent2 = self.select_parents(population)
            child1, child2 = self.crossover(parent1, parent2)
            child1 = self.mutate(child1)
            child2 = self.mutate(child2)
            new_population.extend([child1, child2])
        return new_population

    def run(self) -> List[int]:
        # Initialize population and evolve over generations
        population = self.initialize_population()
        for _ in range(self.generations):
            population = self.evolve_population(population)
        # Select the best solution from the final population
        return max(population, key=self.fitness_function)

# Example usage:
if __name__ == "__main__":
    # Initialize Genetic Algorithm with parameters
    ga = GeneticAlgorithm(population_size=100, chromosome_length=10, generations=100, mutation_rate=0.1)
    # Run the Genetic Algorithm to find the best solution
    best_solution = ga.run()
    print("Best solution:", best_solution)
