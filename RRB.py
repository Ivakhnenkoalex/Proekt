def RRb(lst, steps):
    steps = -1
    if steps < 0:
        lst = lst[1:]+lst[:1]
    else:
        lst = lst[-1:]+lst[:-1]
    return lst
