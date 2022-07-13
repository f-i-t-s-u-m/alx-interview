#!/usr/bin/python3
""" python utf-8 validator file """


def validUTF8(data):
    """ validUTF8 function """
    bo = True
    for i in data:
        if i < 0 or i >= 256:
            bo = False
    return bo
