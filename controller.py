import model
import error


def solve(text: str, priority: int) -> float or str:
    for char in text:
        if char in model.priority_dictionary:  # char is an operator
            if model.priority_dictionary[char] == priority:  # operator is in the correct level of priority
                split = text.split(char, 1)
                if char in model.functions_dict_middle:
                    if char not in model.functions_dict_left or sub_or_neg(str(split[0]), str(split[1])).__eq__("sub"):
                        if char in model.functions_dict_left:
                            model.flag_for_sub_test = True
                        operand1 = solve(str(split[0]), min_priority(str(split[0])))
                        model.flag_for_sub_test = False
                        operand2 = solve(str(split[1]), min_priority(str(split[1])))
                        if are_numbers(str(operand1), str(operand2)):
                            return model.functions_dict_middle[char](str(operand1), str(operand2))
                        else:
                            error.missing_number(char, before_or_after(str(operand1)))
                            return
                if char in model.functions_dict_left or char in model.functions_dict_right:
                    if char in model.functions_dict_left:
                        if char.__eq__('~') or char.__eq__('-'):
                            model.neg += 1
                            model.neg += how_many_minus(str(split[0]))
                        operand2 = solve(split[1], min_priority(split[1]))
                        if is_number(str(operand2)):
                            return model.functions_dict_left[char](str(operand2))
                    elif char in model.functions_dict_right:
                        operand1 = solve(split[0], min_priority(split[0]))
                        if is_number(str(operand1)) and split[1].__eq__(""):
                            return model.functions_dict_right[char](str(operand1))
                        elif not split[1].__eq__(""):
                            slv = str(model.functions_dict_right[char](str(operand1)))
                            slv += split[1]
                            return solve(slv, min_priority(slv))
                    else:
                        error.missing_number(char, before_or_after(str(operand1)))
                        return
        elif not is_number(char) and not char.__eq__('.'):
            error.invalid_character(char)
            return
    if model.got_error:
        return
    elif model.neg != 0 or model.flag_for_sub_test:
        return float(text)
    return text


def before_or_after(operand1: str,) -> str:
    """
    return if num is missing before or after the operator
    :param operand1:
    :return:
    """
    if is_number(operand1):
        return "after"
    return "before"


def are_numbers(operand1: str, operand2: str) -> bool:
    """
    return if both are numbers
    :param operand1:
    :param operand2:
    :return:
    """
    return is_number(operand1) and is_number(operand2)


def is_number(operand: str) -> bool:
    """
    return if operand is number
    :param operand:
    :return:
    """
    if operand.__contains__('-'):
        if not operand.split('-', 1)[0].__eq__("") and not contains_only(operand.split('-', 1)[0], '~')\
                and not contains_only(operand.split('-', 1)[0], '-'):
            return False
    return operand.replace('.', '').replace('-', '').isdigit()


def delete_unwonted_chars(text: str) -> tuple:
    """
    Get rid of irrelevant notes, perform preliminary checks
    and make updates to the equation that will help to solve it
    :param text:
    :return: text to solve
    """
    text = text.replace(" ", "")
    text = text.replace("\t", "")
    if text.__eq__(""):
        error.empty()
        return None, False
    if not check_tilda(text):
        return None, False
    text = handle_signs(text)
    if check_parentheses(text):
        text = handle_parentheses(text)
    if text.count('-') > 1:
        text = add_necessary_parentheses(text, '-')
    if text.count('+') > 1:
        text = add_necessary_parentheses(text, '+')
    if not check_parentheses(text):
        return None, False
    return handle_parentheses(text), True


def handle_signs(text: str) -> str:
    """
    The function reduces combinations of minuses with pluses and tildes
    with the separation of use as sub or as neg
    :param text:
    :return:
    """
    check_minus = text.split("--")
    between_two = 0
    text = ""
    for check in check_minus:
        if check.__eq__("") or not is_number(check):
            if between_two.__eq__(1):
                text += "+"
            between_two = 0
        else:
            between_two += 1
            if between_two.__eq__(2):
                text += "+"
        text += check
    while text.__contains__("~-") or text.__contains__("-~"):
        split = text.split("~-", 1)
        if split[0].__eq__(""):
            text = text.replace("~-", "", 1)
        else:
            text = text.replace("~-", "+", 1)
        split = text.split("-~", 1)
        if split[0].__eq__(""):
            text = text.replace("-~", "", 1)
        else:
            text = text.replace("-~", "+", 1)
    while text.__contains__("+-") or text.__contains__("++") or text.__contains__("-+"):
        text = text.replace("+-", "-")
        text = text.replace("-+", "-")
        text = text.replace("++", "+")
    return text


def min_priority(text: str) -> int:
    """
    Returns the minimum precedence in text
    :param text:
    :return:
    """
    min_prio = model.MAX_PRIORITY
    for char in text:
        if char in model.priority_dictionary:
            if model.priority_dictionary[char] < min_prio:
                min_prio = model.priority_dictionary[char]
    return min_prio


def reset():
    """
    reset the model in the end of equation
    :return:
    """
    model.got_error = False
    model.neg = 0
    model.flag_for_sub_test = False


def handle_parentheses(text: str) -> str:
    """
    In order to treat the parentheses as having first priority,
    the function executes what is inside the parentheses
    (before the large solution function)
    by treating what is in the parentheses as another equation
    and returns the result inside the equation that will be solved later
    :param text:
    :return:
    """
    ret = ""
    solv = ""
    flag_start = False
    for char in text:
        if char.__eq__('('):
            flag_start = True
        elif char.__eq__(')'):
            flag_start = False
            ret += str(solve(solv, min_priority(solv)))
            solv = ret
            ret = ""
            flag_start = True
        elif flag_start:
            solv += char
        else:
            ret += char
    if ret.__eq__(""):
        return solv
    return ret


def check_parentheses(text: str) -> bool:
    """
    Correctness tests of brackets
    :param text:
    :return:
    """
    lst = 0
    flag_start = True
    for char in text:
        if char.__eq__('('):
            flag_start = False
            lst += 1
        elif char.__eq__(')'):
            if not flag_start:
                lst -= 1
                if lst.__eq__(0):
                    flag_start = True
            else:
                return False
    if lst > 0:
        error.invalid_character('(')
        return False
    elif lst < 0:
        error.invalid_character(')')
        return False
    else:
        return True


def check_tilda(text: str) -> bool:
    """
    Correctness tests of tildes
    :param text:
    :return:
    """
    got_tilda = False
    before_is_okay = True
    for char in text:
        if got_tilda:
            if not is_number(char) and not char.__eq__('-') and not char.__eq__(')') and not char.__eq__('('):
                error.tilda_after_tilda()
                return False
            elif is_number(char):
                got_tilda = False
        elif char.__eq__('~'):
            if before_is_okay:
                got_tilda = True
            else:
                error.tilda_after_tilda()
        elif char.__eq__('') or char in model.priority_dictionary or char.__eq__(')') or char.__eq__('('):
            before_is_okay = True
        else:
            before_is_okay = False
    if got_tilda:
        error.missing_number('~', "after")
        return False
    return True


def sub_or_neg(operand1: str, operand2: str) -> str:
    """
    return if the "-" be use as sub or neg minus
    :param operand1:
    :param operand2:
    :return:
    """
    if operand1.__eq__(""):
        return "neg"
    neg_flag = True
    for char in operand1:
        if not char.__eq__("-") and not char.__eq__("~"):
            neg_flag = False
    if neg_flag:
        return "neg"
    rev = operand1[::-1]
    if rev[0] in model.functions_dict_middle:
        return "neg"
    return "sub"


def add_necessary_parentheses(text: str, char: str) -> str:
    """
    Adding parentheses in order to create an order
    of precedence between the same type of operator
    :param text:
    :param char:
    :return:
    """
    ret = ""
    check = text.split(char)
    ret += '('*(len(check)-1)
    for part in check:
        ret += part
        ret += ')'
        ret += char
    print(ret)
    ret = ret[::-1]
    ret = ret.replace(char, '', 1)
    ret = ret.replace(')', '', 1)
    ret = ret[::-1]
    return ret


def how_many_minus(text: str) -> int:
    """
    check how many minuses in text
    :param text:
    :return:
    """
    count = 0
    for char in text:
        if char.__eq__("-") or char.__eq__("~"):
            count += 1
    return count


def contains_only(text: str, char: str) -> bool:
    """
    check if text contains only the char that was giving
    :param text:
    :param char:
    :return:
    """
    for check in text:
        if not check.__eq__(char):
            return False
    return True
