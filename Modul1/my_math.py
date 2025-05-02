def exp(x, n):
    if n < 0:
        raise ValueError('The exponent must be non-negative')
    i, h, r = n, x, 1
    while i > 0:
        # r * h^i = x^n
        if i % 2 == 0:
            h = h * h
            i = i // 2
        else:
            r = r * h
            i = i - 1
    return r

if __name__ == '__main__':
    x = int(input('Base number: '))
    n = int(input('Exponent:    '))
    print(f'{x}^{n} = {exp(x, n)}')