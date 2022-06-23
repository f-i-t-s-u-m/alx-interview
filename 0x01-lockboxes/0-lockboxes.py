#!/usr/bin/python3
""" python interview lock box file """


def canUnlockAll(boxes):
    """ check if box is unlockable """
    myKeys = [0]
    for key in myKeys:
        for boxKey in boxes[key]:
            if boxKey not in myKeys and boxKey < len(boxes):
                myKeys.append(boxKey)
    if len(myKeys) == len(boxes):
        return True
    return False
