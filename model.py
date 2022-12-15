import calculate

priority_dictionary = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5, '~': 6, '!': 6}
functions_dictionary = {'+': calculate.add, '-': calculate.sub, '*': calculate.mul, '/': calculate.div,
                        '^': calculate.power, '%': calculate.modulo, '$': calculate.maximum, '&': calculate.minimum,
                        '@': calculate.avg, '~': calculate.neg, '!': calculate.factorial}
