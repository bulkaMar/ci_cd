def read_population_data(file_name):
    population_data = []
    with open(file_name, 'r') as file:
        for line in file:
            country, area, population = line.strip().split(', ')
            population_data.append((country, float(area), int(population)))
    return population_data


