import input_output
import controller


def main():
    input_output.opening()
    text = input_output.get_input()
    while not text.__eq__("end"):
        text = controller.delete_unwonted_chars(text)
        ret = controller.solve(text, controller.min_priority(text))
        if controller.is_number(str(ret)):
            input_output.print_result(ret)
        text = input_output.get_input()


if __name__ == "__main__":
    main()
