def RRa(a, steps):
    steps = -1
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            a.append(a.pop(0))
    else:
        for i in range(steps):
            a.insert(0, a.pop())
    return a
