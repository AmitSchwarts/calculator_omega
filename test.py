import main


def test_tilda1():
    assert main.program.equation("~3") == -3


def test_tilda2():
    assert main.program.equation("-3") == -3


def test_tilda3():
    assert main.program.equation("~-3") == 3


def test_tilda4():
    assert main.program.equation("--3") == 3


def test_tilda5():
    assert main.program.equation("3+~-3") == 6


def test_tilda6():
    assert main.program.equation("3+-2") == 1


def test_simple1():
    assert main.program.equation("10+13") == 23


def test_simple2():
    assert main.program.equation("10-13") == -3


def test_simple3():
    assert main.program.equation("20-3") == 17


def test_simple4():
    assert main.program.equation("10*3") == 30


def test_simple5():
    assert main.program.equation("10/3") == 3.3333333333333335


def test_simple6():
    assert main.program.equation("12/3") == 4


def test_simple7():
    assert main.program.equation("10%3") == 1


def test_simple8():
    assert main.program.equation("10^3") == 1000


def test_simple9():
    assert main.program.equation("27+3$4") == 31


def test_simple10():
    assert main.program.equation("27@3*4") == 60


def test_simple11():
    assert main.program.equation("27%3^4") == 0


def test_simple12():
    assert main.program.equation("27+3&4") == 30


def test_simple13():
    assert main.program.equation("(~27-3)*4") == -120


def test_simple14():
    assert main.program.equation("5!*2") == 240


def test_simple15():
    assert main.program.equation("(8&2)*7") == 14


def test_simple16():
    assert main.program.equation("7@3$2 + 928#   ") == 24


def test_simple17():
    assert main.program.equation("80@2&50%10 + -~-928#") == -18


def test_simple18():
    assert main.program.equation("5$(4*-123#^2 /12.7@5.3)-100%(12*2.5)") == 6


def test_simple19():
    assert main.program.equation("6!-3^3*2+  (~2/~1+2#)*1-3%2+1") == 670


def test_simple20():
    assert main.program.equation("100&99/33+1.1^2-(3!+~1)%2+7*7") == 52.21


def test_error1():
    main.program.equation("1+")
    assert main.controller.model.got_error is True


def test_error2():
    main.program.equation("1-")
    assert main.controller.model.got_error is True


def test_error3():
    main.program.equation("1~")
    assert main.controller.model.got_error is True


def test_error4():
    main.program.equation("\t\t \t")
    assert main.controller.model.got_error is True


def test_error5():
    main.program.equation("asdfghjj")
    assert main.controller.model.got_error is True


def test_error6():
    main.program.equation("")
    assert main.controller.model.got_error is True


def test_error7():
    main.program.equation("1@!1")
    assert main.controller.model.got_error is True
