def shiftr(lst, steps): ## lst - это или a или b,steps  = 1 если ra или rb,steps = -1 если rra или rrb
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
    return lst
