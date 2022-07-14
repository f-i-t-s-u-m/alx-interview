#!/usr/bin/python3
""" python utf-8 validator file """


def validUTF8(data):
    """ validUTF8 function """
    n_bytes = 0

    for num in data:
        print(format(num, "#010b"))
        if n_bytes == 0:
            for bit in binary:
                if bit == '0':
                    break
                n_bytes += 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if binary[0] != '1' or binary[1] != '0':
                return False

        n_bytes -= 1
    return n_bytes == 0
