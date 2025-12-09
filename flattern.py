def list_flatten(1, a=None):
    a =list(a) if isinstance(a, (list, tuple)) else[]
    for i in l:
        if isinsatnce(i, (list, tuple)):
        a =list_flatten(i,a)
        else:
        a.append(i)

    return a