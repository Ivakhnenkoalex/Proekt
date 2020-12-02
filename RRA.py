def ft_s(m):
    m[0], m[1] = m[1], m[0]
    return m


def RRa(a, steps):
    a = []
    d = len(m)
    if st == 1:
        a.append(m[d-1])
        i = 0
        while i < ft_len(m)-1:
            a.append(m[i])
            i = i + 1
        return a
    if st == -1:
        i = 1
        while i < ft_len(m):
            a.append(m[i])
            i = i + 1
        a.append(m[0])
        return a
