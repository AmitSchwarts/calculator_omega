import model


def solve(text: str, priority: int) -> int or float:
    text = delete_unwonted_chars(text)
    still_complex = False
    for char in text:
        if char in model.priority_dictionary:
            still_complex = True
            if model.priority_dictionary[char] == priority:
                operand1 = solve(text.split(char, 1)[0], priority)
                operand2 = solve(text.split(char, 1)[1], priority)
                if are_numbers(str(operand1), str(operand2)):
                    return model.functions_dictionary[char](str(operand1), str(operand2))
    if still_complex:
        priority += 1
        return solve(text, priority)
    return text


def are_numbers(operand1: str, operand2: str) -> bool:
    if operand1.replace('.', '').replace('-', '').isdigit():
        if operand2.replace('.', '').replace('-', '').isdigit():
            return True
        print(operand2+" is not a number")
        False
    print(operand1 + " is not a number")
    False


def delete_unwonted_chars(text: str) -> str:
    text = text.replace(" ", "")
    text = text.replace("--", "")
    return text



