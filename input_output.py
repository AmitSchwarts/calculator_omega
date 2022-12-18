import error


def opening():
    print("Hello and welcome to the Omega calculator:\n"
          "From this moment on you can enter invoice expressions according to the instructions and get a result.\n"
          "If you want to stop using the calculator, you can type \"end\"\n\n"
          "Instructions for use:\n"
          " + , - , *, / : use for add, sub, mul and div\n"
          " ^ : use for calc power \n"
          " % : use for calc modulo \n"
          " & : use for calc minimum \n"
          " $ : use for calc maximum \n"
          " @ : use for calc average \n"
          " ~ : use for change sign to a number \n"
          " ! : use for calc factorial \n"
          " # : use for calc sum of digits \n\n"
          "lets start :-)\n")


def get_input():
    print("Insert an equation: ")
    try:
        return input()
    except EOFError:
        error.eof_error()
        return


def print_result(result):
    print(result)


def closing():
    print("I hope you enjoy from my calculator - Goodbye")
