def s(m):
    m[0], m[1] = m[1], m[0]
    return m


def shiftr(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())


def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_rev_list(mass):
    a = []
    d = ft_len(mass)
    c = d
    i = 0
    d = d - 1
    while d > i:
        a.append(mass[d])
        d = d - 1
    a.append(mass[0])
    i = 0
    while c > i:
        mass[i] = a[i]
        i = i + 1
    return mass
