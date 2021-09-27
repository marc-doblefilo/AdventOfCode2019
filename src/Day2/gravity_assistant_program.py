def gravity_program(opcodes_list: list):
    return_list: list = opcodes_list

    for index, code in enumerate(return_list):
        if index%4 == 0:
            if return_list[index] == 1:
                first_number = return_list[return_list[index+1]]
                second_number = return_list[return_list[index+2]]
                return_list[return_list[index+3]] = first_number + second_number
            elif return_list[index] == 2:
                first_number = return_list[return_list[index+1]]
                second_number = return_list[return_list[index+2]]
                return_list[return_list[index+3]] = first_number * second_number


    return return_list
