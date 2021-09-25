import math

def fuel_calculator(mass: int):
    return (math.floor(mass/3)-2)

def sum_of_fuels(masses: list):
    sum:int = 0
    for mass in masses:
        sum += fuel_calculator(mass)

    return sum
