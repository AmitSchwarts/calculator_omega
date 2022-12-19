import model


def missing_number(operator: str, before_or_after: str):
    if not model.got_error:
        print("Missing number " + before_or_after + " the operator: " + operator)
        model.got_error = True


def zero_division():
    if not model.got_error:
        print("It is impossible to divide by zero")
        model.got_error = True


def operand_not_int(func: str, operand: str):
    if not model.got_error:
        print(func+" function can't get non int operand: "+operand)
        model.got_error = True


def factorial_negative(operand: str):
    if not model.got_error:
        print("Impossible to activate Factorial function on negative number: -" + operand)
        model.got_error = True


def eof_error():
    if not model.got_error:
        print("Understand you want to close the program")
        model.got_error = True


def empty():
    if not model.got_error:
        print("Got an empty equation")
        model.got_error = True


def invalid_character(char: str):
    if not model.got_error:
        print("Got an invalid_character: "+char)
        model.got_error = True


def tilda_after_tilda():
    if not model.got_error:
        print("Tildes must be separated from each other by numbers")
        model.got_error = True


def zero_power():
    if not model.got_error:
        print("It is impossible to power zero by zero - Undefined expression")
        model.got_error = True


def complex_num():
    if not model.got_error:
        print("Expression is a complex_num")
        model.got_error = True
