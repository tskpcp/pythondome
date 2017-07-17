def frange(start,stop,step=1):
    i=start
    while i<stop:
        yield i
        i+=step
