def shiftr(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
    return lst


def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_pa(a, b): ## a - массив в который добавляешь элемент b - массив из которого добавляешь элемент
    a.append(b[0])
    a = shiftr(a, 1)
    return a
