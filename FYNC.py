def ft_s(m):
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
    return lst


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


def ft_sorted(a):
    b = []
    for j in range(0, ft_len(a)):
        z = 0
        for i in range(0, ft_len(a)):
            if z < a[i]:
                z = a[i]
        if z > 0:
            b.append(z)
            for n in range(0, ft_len(a)):
                if a[n] == z:
                    a[n] = a[n] * 0
    return (ft_rev_list(b))


z = input()
a = []
b = []
while z != '!':
    z = int(z)
    a.append(z)
    z = input()
kon = ft_sorted(a)
min = 1001
while a != kon:
    i = 0
    while i < ft_len(a):
        if a[i] < min: ## Тут что-то не так
            min = a[i]
        i = i + 1
    if a[0] > a[1]:
       a = ft_s(a)
       print(sa)
    if a[0] == min:
        b.append(a[0])
        b = shiftr(b,1)
        print(pb)
    else:
        a = shiftr(a,1)
        print(rra)
    if b == kon:
        i = 0
        while i < ft_len(a):
            a.append(b[0])
            a = shiftr(a,1)
            print(pa)
            a = shiftr(a,-i)
            print(ra)
