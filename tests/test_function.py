import pytest
from main import read_population_data, sort_by_area, sort_by_population


@pytest.fixture
def population_data():
    return [
        ("Italy", 301340.0, 60461826),
        ("Germany", 357022.0, 83783942),
        ("Spain", 505990.0, 47329981),
    ]


def test_read_population_data(tmp_path, population_data):
   
    file_path = tmp_path / "test_population_data.txt"
    with open(file_path, "w") as f:
        for country, area, population in population_data:
            f.write(f"{country}, {area}, {population}\n")

    
    assert read_population_data(file_path) == population_data
    
    
def test_sort_by_area(population_data):
    
    expected_result = [("Italy", 301340.0, 60461826),
                       ("Germany", 357022.0, 83783942),
                       ("Spain", 505990.0, 47329981)]

   
    assert sort_by_area(population_data) == expected_result
    

def test_sort_by_population(population_data):
    
    expected_result = [("Spain", 505990.0, 47329981),
                       ("Italy", 301340.0, 60461826),
                       ("Germany", 357022.0, 83783942)]

    
    assert sort_by_population(population_data) == expected_result
    
    
    