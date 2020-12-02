def Ra(lst,steps=1): ## lst - это или a или b,steps  = 1 если ra или rb,steps = -1 если rra или rrb
    if steps < 0:
        lst = lst[1:]+lst[:1]
    else:
        lst = lst[-1:]+lst[:-1]
    return lst
