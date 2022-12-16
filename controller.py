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
                        error.print_error("not a number - ", what_not_number(str(operand1), str(operand2)))
                elif char in model.functions_dict_left:
                    if is_number(str(operand2)):
                        return model.functions_dict_left[char](str(operand2))
                elif char in model.functions_dict_right:
                    if is_number(str(operand1)):
                        return model.functions_dict_right[char](str(operand1))
    return text


def what_not_number(operand1: str, operand2: str) -> bool:
    if is_number(operand1):
        return operand2
    return operand1


def are_numbers(operand1: str, operand2: str) -> bool:
    return is_number(operand1) and is_number(operand2)


def is_number(operand: str) -> bool:
    if operand.replace('.', '').replace('-', '').isdigit():
        return True
    return False


def delete_unwonted_chars(text: str) -> str:
    text = text.replace(" ", "")
    text = handle_signs(text)
    return text


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
