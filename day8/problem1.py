import operator
from collections import defaultdict

operators = {
    "<": operator.lt,
    ">": operator.gt,
    "==": operator.eq,
    "!=": operator.ne,
    ">=": operator.ge,
    "<=": operator.le
}

def identify_variables(instruction_string):
    tokens = instruction_string.split(" ")
    variable_to_modify = tokens[0] # modify variable always first string before first space
    conditional_variable = tokens[tokens.index("if") + 1] # variable used in conditional should be after "if"
    return {variable_to_modify: 0, conditional_variable: 0}

def perform_operation(state, instruction_string):
    tokens = instruction_string.split(" ")
    variable_to_modify = tokens[0]
    new_state = state
    if evaluate_condition(new_state, tokens[tokens.index("if")+1:]):
        if tokens[1] == "inc":
            new_state[variable_to_modify] += int(tokens[2])
        else:
            new_state[variable_to_modify] -= int(tokens[2])

    return new_state

def evaluate_condition(state, conditional_tokens):
    conditional_variable = conditional_tokens[0]
    operator = conditional_tokens[1]
    operand = int(conditional_tokens[2])
    return operators[operator](state[conditional_variable], operand)

def apply_operations(filename):
    with open(filename, 'r') as instructions_file:
        state = defaultdict(int)
        largest_value = None
        for instruction in instructions_file:
            state = perform_operation(state, instruction.strip())
            instruction_largest_value = find_largest_value(state)
            if largest_value:
                if instruction_largest_value > largest_value:
                    largest_value = instruction_largest_value
            else:
                largest_value = instruction_largest_value

    return state, largest_value

def find_largest_value(state):
    largest_value = max(state.values())
    return largest_value

# state, largest_value = apply_operations("input.txt")
# print(state)
# print(find_largest_value(state))
