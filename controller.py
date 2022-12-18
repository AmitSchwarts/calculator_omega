import model
import error


def solve(text: str, priority: int) -> float or str:
    for char in text:
        if char in model.priority_dictionary:
            if model.priority_dictionary[char] == priority:
                split = text.split(char, 1)
                if char in model.functions_dict_middle:
                    if char not in model.functions_dict_left or sub_or_neg(str(split[0]), str(split[1])).__eq__("sub"):
                        operand1 = solve(str(split[0]), min_priority(str(split[0])))
                        operand2 = solve(str(split[1]), min_priority(str(split[1])))
                        if are_numbers(str(operand1), str(operand2)):
                            return model.functions_dict_middle[char](str(operand1), str(operand2))
                        else:
                            error.missing_number(char, before_or_after(str(operand1), str(operand2)))
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
                        if is_number(str(operand1)):
                            return model.functions_dict_right[char](str(operand1))
                    else:
                        error.missing_number(char, before_or_after(str(operand1), str(operand2)))
                        return
        elif not is_number(char) and not char.__eq__('.'):
            error.invalid_character(char)
            return
    return text


def before_or_after(operand1: str, operand2: str) -> str:
    if is_number(operand1):
        return "after"
    return "before"


def are_numbers(operand1: str, operand2: str) -> bool:
    return is_number(operand1) and is_number(operand2)


def is_number(operand: str) -> bool:
    return operand.replace('.', '').replace('-', '').isdigit()


def delete_unwonted_chars(text: str) -> tuple:
    text = text.replace(" ", "")
    text = text.replace("\t", "")
    if text.__eq__(""):
        error.empty()
        return None, False
    text = handle_signs(text)
    if not check_tilda(text):
        return None, False
    if text.__contains__('-'):
        text = add_necessary_parentheses(text, '-')
    if not check_parentheses(text):
        return None, False
    return handle_parentheses(text), True


def handle_signs(text: str) -> str:
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
    while text.__contains__("+-") or text.__contains__("++") or text.__contains__("-+"):
        text = text.replace("+-", "-")
        text = text.replace("-+", "-")
        text = text.replace("++", "+")
    return text


def min_priority(text: str) -> int:
    min_prio = model.MAX_PRIORITY
    for char in text:
        if char in model.priority_dictionary:
            if model.priority_dictionary[char] < min_prio:
                min_prio = model.priority_dictionary[char]
    return min_prio


def reset():
    model.got_error = False


def handle_parentheses(text: str) -> str:
    ret = ""
    solv = ""
    flag_start = False
    for char in text:
        if char.__eq__('('):
            flag_start = True
        elif char.__eq__(')'):
            flag_start = False
            ret += str(solve(solv, min_priority(solv)))
            solv = ""
        elif flag_start:
            solv += char
        else:
            ret += char
    return ret


def check_parentheses(text: str) -> bool:
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
        elif char.__eq__('') or char in model.priority_dictionary:
            before_is_okay = True
        else:
            before_is_okay = False
    if got_tilda:
        error.missing_number('~', "after")
        return False
    return True


def sub_or_neg(operand1: str, operand2: str) -> str:
    if operand1.__eq__(""):
        return "neg"
    for char in operand1:
        if not char.__eq__("-") and not char.__eq__("~"):
            return "sub"
    return "neg"


def add_necessary_parentheses(text: str, char) -> str:
    ret = ""
    every_two = 0
    check = text.split(char)
    ret += '('*(len(check)-1)
    for part in check:
        ret += part
        every_two += 1
        if every_two.__eq__(2):
            ret += ')'
            every_two = 1
        ret += char
    ret = ret[::-1]
    ret = ret.replace(char, '', 1)
    ret = ret[::-1]
    return ret


def how_many_minus(text: str) -> int:
    count = 0
    for char in text:
        if char.__eq__("-") or char.__eq__("~"):
            count += 1
    return count
