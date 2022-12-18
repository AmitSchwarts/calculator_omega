import math
import error
import controller


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
    return div(add(operand1, operand2), 2.0)


def neg(operand: str) -> float:
    return -float(operand)


def factorial(operand: str) -> int:
    if operand.__contains__('~') or operand.__contains__('-'):
        error.factorial_operand_not_int(operand)
        return
    try:
        ret = 1
        for num in range(2, int(operand)+1):
            ret = mul(ret, num)
        return ret
    except ValueError:
        error.factorial_operand_not_int(operand)


def sum_digits(operand: str) -> int:
    work_on = 0
    ret = 0
    for char in operand:
        ret += float(char)
    while ret > 10:
        work_on = ret
        ret = 0
        for char in work_on:
            ret += float(char)
    return ret
