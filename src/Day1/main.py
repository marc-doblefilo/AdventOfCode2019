from fuelcalculator import *

if __name__ == "__main__":
    list_of_masses: list = []

    with open('src/Day1/input.txt', 'r') as file:
        for line in file:
            list_of_masses.append(int(line))

    print("Day 1 - Part One: " + str(sum_of_fuels(list_of_masses)))
