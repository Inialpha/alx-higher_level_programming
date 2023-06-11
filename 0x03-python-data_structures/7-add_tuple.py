#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    ln_a = len(tuple_a)
    ln_b = len(tuple_b)
    if ln_a > ln_b:
        ln = ln_a
    else:
        ln = ln_b
    new_t = []
    if ln == 0:
        new = tuple(tuple_a, tuple_b)
        return new
    for i in range(ln):
        a = tuple_a[i] if i < len(tuple_a) else 0
        b = tuple_b[i] if i < len(tuple_b) else 0
        new_t.append(a + b)
    new_t = tuple(new_t)
    return new_t
