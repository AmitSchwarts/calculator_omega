import input_output
import controller
import unittest


class program(unittest.TestCase):
    @staticmethod
    def main():
        input_output.opening()
        text = input_output.get_input()
        while not text.__eq__("end"):
            ret = program.turn(text)
            if controller.is_number(str(ret)) and not controller.model.got_error:
                input_output.print_result(ret)
            controller.reset()
            text = input_output.get_input()
        input_output.closing()

    @staticmethod
    def turn(text: str):

        text, check = controller.delete_unwonted_chars(text)
        if check:
            if controller.is_number(text):
                ret = text
            ret = controller.solve(text, controller.min_priority(text))
        if not controller.model.got_error:
            return ret


if __name__ == "__main__":
    program.main()
