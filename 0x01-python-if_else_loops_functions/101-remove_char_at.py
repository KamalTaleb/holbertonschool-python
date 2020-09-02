#!/usr/bin/python3
def remove_char_at(str, n):
    st = ""
    cont = 0
    for c in str:
        if cont == n:
            pass
        else:
            st += c
        cont += 1
    return st
