def solution(l):
    # Your code here
    r = []
    ret = []
    # create tuples of 3 items, the integer and sort them by major,minor,rest
    for e in range(len(l)):
        st = l[e].split('.')
        if(len(st) == 3):
            r.append((int(st[0]), int(st[1]), int(st[2])))
        elif (len(st) == 2):
            r.append((int(st[0]), int(st[1]), -1))
        else:
            r.append((int(st[0]), -1, -1))

    # sort the tuples first by major, then by minor and rest
    r = sorted(r, key=lambda a: (a[0], a[1], a[2]))

    # convert the tuple back to list of strings
    for e in r:
        entry = str(e[0])
        if e[1] != -1:
            entry += '.' + str(e[1])
        if e[2] != -1:
            entry += '.' + str(e[2])
        ret.append(entry)

    return ret


lista = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]

print(solution(lista))
