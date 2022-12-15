import input_output
import controller

START_PRIORITY = 1


def main():
    input_output.opening()
    text = input_output.get_input()
    while not text.__eq__("end"):
        ret = controller.solve(text, START_PRIORITY)
        if ret is not None:
            input_output.print_result(ret)
        text = input_output.get_input()


if __name__ == "__main__":
    main()
