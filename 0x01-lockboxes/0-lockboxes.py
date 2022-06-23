#!/usr/bin/env python3
""" python interview lock box file """


def canUnlockAll(list):
    """ check if box is unlockable """
    e = False
    for x in list:
        if len(x) and e:
            return False
        elif len(x) == 0:
            e = True
    return True
