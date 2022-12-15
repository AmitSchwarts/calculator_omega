import math


def add(operand1: str, operand2: str) -> float:
    return float(operand1) + float(operand2)


def sub(operand1: str, operand2: str) -> float:
    return float(operand1) - float(operand2)


def mul(operand1: str, operand2: str) -> float:
    return float(operand1) * float(operand2)


def div(operand1: str, operand2: str) -> int:
    return float(operand1) / float(operand2)


def power(operand1: str, operand2: str) -> int or float:
    return math.pow(float(operand1), float(operand2))


def modulo(operand1: str, operand2: str) -> int:
    return float(operand1) % float(operand2)


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
    return (operand1+operand2) / 2.0


def neg(operand: str) -> str:
    return "-"+operand


def factorial(operand: str) -> int:
    ret = 1
    for num in range(2, float(operand) + 1):
        ret = ret * num
    return ret
