import model
import error


def solve(text: str, priority: int) -> float or str:
    for char in text:
        if char in model.priority_dictionary:
            if model.priority_dictionary[char] == priority:
                split = text.split(char, 1)
                operand1 = solve(split[0], min_priority(split[0]))
                operand2 = solve(split[1], min_priority(split[1]))
                if char in model.functions_dict_middle:
                    if are_numbers(str(operand1), str(operand2)):
                        return model.functions_dict_middle[char](str(operand1), str(operand2))
                    elif char not in model.functions_dict_left:
                        error.missing_number(char, before_or_after(str(operand1), str(operand2)))
                if char in model.functions_dict_left or char in model.functions_dict_right:
                    if char in model.functions_dict_left and is_number(str(operand2)):
                        if not is_number(str(operand1)):
                            return model.functions_dict_left[char](str(operand2))
                        else:
                            error.invalid_character(str(operand1))
                    elif char in model.functions_dict_right and is_number(str(operand1)):
                        if not is_number(str(operand2)):
                            return model.functions_dict_right[char](str(operand1))
                        else:
                            error.invalid_character(str(operand2))
                    else:
                        error.missing_number(char, before_or_after(str(operand1), str(operand2)))
        elif not is_number(char) and not char.__eq__('.'):
            error.invalid_character(char)
    return text


def before_or_after(operand1: str, operand2: str) -> str:
    if is_number(operand1):
        return "after"
    return "before"


def are_numbers(operand1: str, operand2: str) -> bool:
    return is_number(operand1) and is_number(operand2)


def is_number(operand: str) -> bool:
    return operand.replace('.', '').replace('-', '').isdigit()


def delete_unwonted_chars(text: str) -> str:
    text = text.replace(" ", "")
    text = text.replace("\t", "")
    if text.__eq__(""):
        error.empty()
        return None, False
    if not check_tilda(text):
        return None, False
    text = handle_tilda(text)
    text = handle_signs(text)
    if not check_parentheses(text):
        return None, False
    return handle_parentheses(text), True


def handle_signs(text: str) -> str:
    check_minus = text.split("--")
    between_two = 0
    text = ""
    for check in check_minus:
        if check.__eq__(""):
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
        elif not flag_start:
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
                flag_start = True
                lst -= 1
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
    for char in text:
        if got_tilda:
            if not is_number(char) and not char.__eq__('-'):
                error.tilda_after_tilda()
                return False
            elif is_number(char):
                got_tilda = False
        if char.__eq__('~'):
            got_tilda = True
    if got_tilda:
        error.missing_number('~', "after")
        return False
    return True


def handle_tilda(text: str):
    ret = ""
    num_before = False
    for char in text:
        if char.__eq__('~'):
            if num_before:
                ret += '-'
            else:
                ret += '~'
                num_before = False
        elif char.__eq__('-'):
            if num_before:
                ret += '-'
            else:
                ret += '~'
                num_before = False
        elif is_number(char) or char.__eq__('.'):
            num_before = True
            ret += char
        else:
            num_before = False
            ret += char
    return ret

