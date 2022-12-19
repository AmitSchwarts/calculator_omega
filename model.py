import calculate

MIN_PRIORITY = 1
MAX_PRIORITY = 6
priority_dictionary = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5, '~': 6, '!': 6, '#': 6}
functions_dict_middle = {'+': calculate.add, '-': calculate.sub, '*': calculate.mul, '/': calculate.div,
                         '^': calculate.power, '%': calculate.modulo, '$': calculate.maximum, '&': calculate.minimum,
                         '@': calculate.avg}
functions_dict_left = {'~': calculate.neg, '-': calculate.neg}
functions_dict_right = {'!': calculate.factorial, '#': calculate.sum_digits}
got_error = False
neg = 0
flag_for_the_test = False
