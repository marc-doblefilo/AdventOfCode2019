from fuelcalculator import fuel_calculator, sum_of_fuel_calculator

## PART ONE ##

def test_mass_of_12_returns_2():
    assert fuel_calculator(12)==2

def test_mass_of_14_returns_2():
    assert fuel_calculator(14)==2

def test_mass_of_1969_returns_654():
    assert fuel_calculator(1969)==654

def test_mass_of_100756_returns_33583():
    assert fuel_calculator(100756)==33583

## PART TWO ##

def test_module_of_mass_14_requires_2_fuel():
    assert sum_of_fuel_calculator(14)==2

def test_module_of_mass_1969_requires_966_fuel():
    assert sum_of_fuel_calculator(1969)==966

def test_module_of_mass_100756_requires_50346_fuel():
    assert sum_of_fuel_calculator(100756)==50346
