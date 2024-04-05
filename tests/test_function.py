import pytest
from main import read_population_data, sort_by_area, sort_by_population


@pytest.fixture
def population_data():
    return [
        ("Italy", 301340.0, 60461826),
        ("Germany", 357022.0, 83783942),
        ("Spain", 505990.0, 47329981),
    ]

