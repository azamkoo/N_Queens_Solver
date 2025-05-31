import random

def fitness(chromosome):
    n = len(chromosome)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if chromosome[i] == chromosome[j]:
                conflicts += 1
            if abs(chromosome[i] - chromosome[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def crossover(parent1, parent2):
    n = len(parent1)
    point = random.randint(1, n - 2)
    child = parent1[:point] + parent2[point:]
    return child

def mutate(chromosome, mutation_rate=0.1):
    n = len(chromosome)
    if random.random() < mutation_rate:
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

def chromosome_to_board(chromosome):
    n = len(chromosome)
    board = []
    for i in range(n):
        row = ['.'] * n
        row[chromosome[i]] = 'Q'
        board.append("".join(row))
    return board

def solve_n_queens_genetic(n, population_size=100, max_generations=1000):
    population = [random.sample(range(n), n) for _ in range(population_size)]

    for generation in range(max_generations):
        population.sort(key=fitness)
        if fitness(population[0]) == 0:
            solution = chromosome_to_board(population[0])
            return [solution]

        retain_length = int(population_size * 0.2)
        parents = population[:retain_length]

        desired_length = population_size - retain_length
        children = []
        while len(children) < desired_length:
            father = random.choice(parents)
            mother = random.choice(parents)
            if father != mother:
                child = crossover(father, mother)
                child = mutate(child)
                children.append(child)

               
                print(f"generetion {generation} - child {len(children)}: {child}")
              

        population = parents + children

    return []


solutions = solve_n_queens_genetic(8)

if solutions:
    print("final")
    for row in solutions[0]:
        print(row)
else:
    print("not found")
