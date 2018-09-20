def consumer():
    i, y = -1, None
    while True:
        x = yield (i, y)
        y = x
        i += 1


def consume(g):
    c = consumer()
    c.send(None)
    while True:
        try:
            x = next(g)
        except StopIteration:
            break
        y = c.send(x)
        print y


g = iter('abcdefghijklmnopqrstuvwxyz')
consume(g)

