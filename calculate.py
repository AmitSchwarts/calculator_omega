import math


def add(oper1, oper2):
    return oper1 + oper2


def sub(oper1, oper2):
    return oper1 - oper2


def mul(oper1, oper2):
    return oper1 * oper2


def div(oper1, oper2):
    return oper1 / oper2


def power(oper1, oper2):
    return math.pow(oper1, oper2)


def modulo(oper1, oper2):
    return oper1 % oper2


def max(oper1, oper2):
    if oper1 > oper2:
        return oper1
    return oper2


def min(oper1, oper2):
    if oper1 < oper2:
        return oper1
    return oper2


def avg(oper1, oper2):
    return (oper1 + oper2) / 2


def neg(oper):
    return -oper


def fuct(oper):
    ret = 1
    for num in range(2, oper + 1):
        ret = ret * num
    return ret
