# Define a function that validates correct encapsulation of expression in square brackets. (The expresion itself doesn't have to be correct. Only brackets must be placed correctly.)


def validate():
    # TODO: define the body here!
    pass


validate('[a + 1] - [a + 2]')  # Expected true
validate('[[b]]]')  # Expected false
validate('][x + z -[a]+[1 - [2]'). # Expected false
