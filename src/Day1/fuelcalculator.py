import math

def fuel_calculator(mass: int):
    return (math.floor(mass/3)-2)

def sum_of_fuels(masses: list):
    sum:int = 0
    for mass in masses:
        sum += fuel_calculator(mass)

    return sum

def sum_of_fuel_calculator(mass: int):
    sum: int = 0
    left_mass: int = fuel_calculator(mass)
    sum += left_mass
    while fuel_calculator(left_mass) > 0:
        sum += fuel_calculator(left_mass)
        left_mass = fuel_calculator(left_mass)

    return sum

def sum_of_sums_of_fuels(masses: list):
    sum: int = 0
    for mass in masses:
        sum += sum_of_fuel_calculator(mass)

    return sum
