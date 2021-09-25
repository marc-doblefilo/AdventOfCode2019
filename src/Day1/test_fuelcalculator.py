from fuelcalculator import fuel_calculator

def test_mass_of_12_returns_2():
    assert fuel_calculator(12)==2

def test_mass_of_14_returns_2():
    assert fuel_calculator(14)==2

def test_mass_of_1969_returns_654():
    assert fuel_calculator(1969)==654

def test_mass_of_100756_returns_33583():
    assert fuel_calculator(100756)==33583
