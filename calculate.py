import math
import error
import model


def add(operand1: str, operand2: str) -> float:
    return float(operand1) + float(operand2)


def sub(operand1: str, operand2: str) -> float:
    return float(operand1) - float(operand2)


def mul(operand1: str, operand2: str) -> float:
    return float(operand1) * float(operand2)


def div(operand1: str, operand2: str) -> float:
    try:
        return float(operand1) / float(operand2)
    except ZeroDivisionError:
        error.zero_division()


def power(operand1: str, operand2: str) -> float:
    if operand1.__eq__('0') and operand2.__eq__('0'):
        error.zero_power()
        return
    solv = math.pow(float(operand1), float(operand2))
    if type(solv) is complex:
        error.complex_num()
        return
    return solv


def modulo(operand1: str, operand2: str) -> float:
    try:
        return float(operand1) % float(operand2)
    except ZeroDivisionError:
        error.zero_division()


def maximum(operand1: str, operand2: str) -> float:
    operand1 = float(operand1)
    operand2 = float(operand2)
    if operand1 > operand2:
        return operand1
    return operand2


def minimum(operand1: str, operand2: str) -> float:
    operand1 = float(operand1)
    operand2 = float(operand2)
    if operand1 < operand2:
        return operand1
    return operand2


def avg(operand1: str, operand2: str) -> float:
    return div(str(add(operand1, operand2)), str(2.0))


def neg(operand: str) -> float:
    return -float(operand)


def factorial(operand: str) -> int:
    if operand.__contains__('~') or operand.__contains__('-') or not model.neg % 2 == 0:
        error.factorial_negative(operand)
        return
    try:
        ret = 1
        for num in range(2, int(float(operand)) + 1):
            ret = mul(str(ret), str(num))
        return ret
    except ValueError:
        error.operand_not_int("factorial", operand)


def sum_digits(operand: str) -> int:
    ret = 0
    for char in operand:
        if not char.__eq__('.'):
            ret += float(char)
    return ret
