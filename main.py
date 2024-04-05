def read_population_data(file_name):
    """
    Приймає рядок file_name, який представляє ім'я файлу із даними про популяцію.
    Повертає список кортежів, де кожен кортеж містить інформацію про країну у форматі (назва, площа, населення).
    """
    population_data = []
    with open(file_name, 'r') as file:
        for line in file:
            country, area, population = line.strip().split(', ')
            population_data.append((country, float(area), int(population)))
    return population_data


def sort_by_area(population_data):
    """
    Приймає список кортежів population_data, де кожен кортеж містить інформацію про країну у форматі (назва, площа, населення).
    Повертає список кортежів, відсортований за зростанням площі країн.
    """
    return sorted(population_data, key=lambda x: x[1])



def sort_by_population(population_data):
    """
    Приймає список кортежів population_data, де кожен кортеж містить інформацію про країну у форматі (назва, площа, населення).
    Повертає список кортежів, відсортований за зростанням населення країн.
    """
    return sorted(population_data, key=lambda x: x[2])


