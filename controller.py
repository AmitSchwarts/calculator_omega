import model


def solve(text: str, priority: int) -> float:
    text = delete_unwonted_chars(text)
    still_complex = False
    for char in text:
        if char in model.priority_dictionary:
            still_complex = True
            if model.priority_dictionary[char] == priority:
                operand1 = solve(text.split(char, 1)[0], priority)
                operand2 = solve(text.split(char, 1)[1], priority)
                if char.__eq__("!") and operand2.__eq__("") and is_number(str(operand1)):
                    return model.functions_dictionary[char](str(operand1))
                elif char.__eq__("~") and operand1.__eq__("") and is_number(str(operand2)):
                    return model.functions_dictionary[char](str(operand2))
                if are_numbers(str(operand1), str(operand2)):
                    return model.functions_dictionary[char](str(operand1), str(operand2))
    if still_complex:
        priority += 1
        return solve(text, priority)
    return text


def are_numbers(operand1: str, operand2: str) -> bool:
    return is_number(operand1) and is_number(operand2)


def is_number(operand: str) -> bool:
    if operand.replace('.', '').replace('-', '').isdigit():
        return True
    print(operand+" is not a number")
    return False


def delete_unwonted_chars(text: str) -> str:
    text = text.replace(" ", "")
    text = text.replace("--", "")
    return text



