import main


def test_simple1():
    assert main.program.equation("27+3") == 30


def test_simple2():
    assert main.program.equation("27-3") == 24


def test_simple3():
    assert main.program.equation("27*3") == 81


def test_simple4():
    assert main.program.equation("27/3") == 9


def test_simple5():
    assert main.program.equation("27%3") == 0


def test_simple6():
    assert main.program.equation("27^3") == 19683


def test_simple7():
    assert main.program.equation("27+3$4") == 31


def test_simple8():
    assert main.program.equation("27@3*4") == 60


def test_simple9():
    assert main.program.equation("27%3^4") == 0


def test_simple10():
    assert main.program.equation("27+3&4") == 30


def test_simple11():
    assert main.program.equation("(~27-3)*4") == -120


def test_simple12():
    assert main.program.equation("5!*2") == 240


def test_simple13():
    assert main.program.equation("(8&2)*7") == 14


def test_simple14():
    assert main.program.equation("7@3$2 + 928#   ") == 6


def test_simple15():
    assert main.program.equation("80@2&50%10 + -~-928#") == 0
