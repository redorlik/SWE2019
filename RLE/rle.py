
def rle(mess):
    old = mess[0]
    count = 1
    res = []
    for c in mess[1:]:
        if c == old:
            count += 1
        else:
            res.append(f'{count}{old}')
            count = 1
            old = c
    res.append(f'{count}{old}')
    return ''.join(res)
