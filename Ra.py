def Ra(lst,steps): ## lst - это или a или b,steps  = 1 если ra или rb,steps = -1 если rra или rrb
    steps = 1
    if steps < 0:
        lst = lst[1:]+lst[:1]
    else:
        lst = lst[-1:]+lst[:-1]
    return lst
