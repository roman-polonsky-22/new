import pytest

@pytest.fixture()
def setup_list():
    print("In fixtures")
    city = ['New York', 'London', 'Riyadh', 'Singapore', 'Mumbai']
    return city

def test_getItem(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == 'New York'
    assert setup_list[::2] == ['New York', 'Riyadh', 'Mumbai']