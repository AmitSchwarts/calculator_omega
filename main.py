import input_output
import controller
import unittest


class program(unittest.TestCase):
    @staticmethod
    def main():
        """
        main function - start program
        :return: void - its finish when the program will end
        """
        input_output.opening()
        text = input_output.get_input()
        while not text.__eq__("end"):
            controller.reset()
            ret = program.equation(text)
            if controller.is_number(str(ret)) and not controller.model.got_error:
                input_output.print_result(ret)
            text = input_output.get_input()
        input_output.closing()

    @staticmethod
    def equation(text: str):
        """
        solve one equation
        :param text: to solve
        :return: the answer
        """
        text, check = controller.delete_unwonted_chars(text)
        if check:
            if controller.is_number(text):
                ret = text
            ret = controller.solve(text, controller.min_priority(text))
        if not controller.model.got_error:
            return ret
        controller.reset()


if __name__ == "__main__":
    program.main()
