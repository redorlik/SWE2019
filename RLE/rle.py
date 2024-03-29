import time
class MyException(Exception):
    pass

def encode(mess):

    if type(mess) != str:
        raise MyException()
    if not mess:
        return []
    old = mess[0]
    count = 1
    res = []
    for c in mess[1:]:
        if c == old:
            count += 1
        else:
            res.append((count,old))
            count = 1
            old = c
    res.append((count,old))
    return res

def decode(mess):
    x = [c*i for i,c in mess]
    return ''.join(x)

if __name__ == '__main__':
    import sys
    argv = sys.argv
    if '-e' in argv:
        filename = argv[argv.index('-e')+1]
        func = encode # func er en funktion. Her er det encode
    elif '-d' in argv:
        filename = argv[argv.index('-d')+1]
        func = decode # func er en funktion. Her er det decode
    else:
        filename = argv[-1]
        func = lambda x: decode(encode(x)) # func er en funktion. Her decode(encode(x))
    with open(filename,'r') as f:
        print(func(f.read()))
    # Denne pause er nødvendig for at fuzzeren kan skelne
    # mellem crash og succes (en fejl i fuzzzeren)
    time.sleep(1)
    exit(0)
