

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


def main():
    """
    Головна функція програми. Виконує зчитування даних, сортування та вивід результатів.
    """
    file_name = "information.txt" 
    try:
        population_data = read_population_data(file_name)
        sorted_by_area = sort_by_area(population_data)
        sorted_by_population = sort_by_population(population_data)

        print("Data sorted by area:")
        for country, area, population in sorted_by_area:
            print(f"{country}: area - {area}, population - {population}")

        print("\nData sorted by population:")
        for country, area, population in sorted_by_population:
            print(f"{country}: area - {area}, population - {population}")

    except FileNotFoundError:
        print("File doesn't find.")
    except ValueError:
        print("The data format in the file is incorrect.")

if __name__ == "__main__":
    main()