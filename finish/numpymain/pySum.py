def pySum():
    a=list(range(10000))
    b=list(range(10000))
    c=list()
    for i in range(len(a)):
        c.append(a[i]**2+b[i]**2)
    return c