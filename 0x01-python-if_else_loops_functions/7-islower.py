#!/usr/bin/python3
def islower(c):
    for i in range(67, 123):
        if ord(c) >= i:
            return True
        else:
            return False
