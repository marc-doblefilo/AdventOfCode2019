from gravity_assistant_program import *

if __name__ == "__main__":
    list_of_numbers: list = []
    with open('src/Day2/input.txt' ,'r') as file:
        for line in file:
            list_of_numbers = list(line.split(","))


    print("Day 2 - Part One: " + str(gravity_program(list_of_numbers)[0]))
