import input_output
import controller


def main():
    input_output.opening()
    text = input_output.get_input()
    while not text.__eq__("end"):
        text, check = controller.delete_unwonted_chars(text)
        if check:
            ret = controller.solve(text, controller.min_priority(text))
            if controller.is_number(str(ret)) and not controller.model.got_error:
                input_output.print_result(ret)
        controller.reset()
        text = input_output.get_input()
    input_output.closing()


if __name__ == "__main__":
    main()
