#!/usr/bin/python3
""" python utf-8 validator file """


def validUTF8(data):
    """ validUTF8 function """
    bo = True
    for i in data:
        try:
            bytes.fromhex(hex(i)[2:]).decode()
        except ValueError:
            bo = False
    return bo
