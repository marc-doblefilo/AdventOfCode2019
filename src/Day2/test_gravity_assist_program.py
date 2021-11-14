from gravity_assistant_program import *

def test_100099_becomes_200099():
    test_list = [1, 0, 0, 0, 99]
    expected_list = [2, 0, 0, 0, 99]
    assert gravity_program(test_list) == expected_list

def test_230399_becomes_230699():
    test_list = [2, 3, 0, 3, 99]
    expected_list = [2, 3, 0, 6, 99]
    assert gravity_program(test_list) == expected_list

def test_2445990_becomes_2445999801():
    test_list = [2, 4, 4, 5, 99, 0]
    expected_list = [2, 4, 4, 5, 99, 9801]
    assert gravity_program(test_list) == expected_list

def test_11149956099():
    test_list = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    expected_list = [30, 1, 1, 4, 2, 5, 6, 0, 99]
    assert gravity_program(test_list) == expected_list


