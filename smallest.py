INFINITY = float('inf')

def smallest_two(v):
    min1 = INFINITY
    min2 = INFINITY
    i = 0

    while i < len(v):
        if v[i] < min1:
            min2 = min1
            min1 = v[i]
        elif v[i] < min2:
            min2 = v[i]
        i += 1

    if min1 == INFINITY:
        return (INFINITY, INFINITY)
    if min2 == INFINITY:
        return (min1, INFINITY)
    
    return (min1, min2)

    
    
    