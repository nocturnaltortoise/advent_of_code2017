from problem1 import *

def test_variables_correctly_identified():
    test_string = "b inc 5 if a > 1"
    assert identify_variables(test_string) == {"b": 0, "a": 0}

def test_multi_character_vars_identified():
    test_string = "xyz inc 5 if bsqw > 1"
    assert identify_variables(test_string) == {"xyz": 0, "bsqw": 0}

def test_perform_correct_op_with_false_condition():
    initial_state = {"a": 0, "b": 0}
    test_string = "b inc 5 if a > 1"
    assert perform_operation(initial_state, test_string) == {"a": 0, "b": 0}

def test_perform_correct_op_with_true_condition():
    initial_state = {"a": 0, "b": 0}
    test_string = "b inc 5 if a < 1"
    assert perform_operation(initial_state, test_string) == {"a": 0, "b": 5}

def test_multiple_operations_performed_correct():
    filename = "test_input.txt"
    # check that correct state is found, and the correct maximum value at any point is also found
    assert apply_operations(filename) == ({"a": 1, "b": 0, "c": -10}, 10)

def test_find_largest_value():
    state = {"a": 0, "b": 1}
    assert find_largest_value(state) == 1
