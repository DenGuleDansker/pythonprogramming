from math import sqrt

print("Opgave 1")
#Incrementing
print("Increment")
def increment(v):
    if len(v) == 0:
        raise ValueError("List is empty")
    i = 0
    newlst = []
    while i < len(v):
        v[i] = v[i] + 1
        newlst.append(v[i])
        i = i + 1    
    return newlst

print(increment([1, 2, 3]))


print("-----------------------------------------------------------------------------------------------")
print("Opgave 2")
print("Double")
# Double
def double(v):
    if len(v) == 0:
        raise ValueError("List is empty")
    i = 0
    while i < len(v):
        v[i] = v[i] * 2
        i = i + 1
    return v

print(double([1, 2, 3]))

print("-----------------------------------------------------------------------------------------------")
print("Opgave 3")
print("Squared")
# Squared
def squared(v):
    if len(v) == 0:
        raise ValueError("List is empty")
    i = 0
    squaredlst = []
    while i < len(v):
        v[i] = v[i] * v[i]
        squaredlst.append(v[i])
        i = i + 1
    return squaredlst

print(squared([1, 2, 3]))

print("-----------------------------------------------------------------------------------------------")
print("Opgave 4")
print("Lengths")
# Lengths
def lengths(v):
    if len(v) == 0:
        raise ValueError("List is empty")
    i = 0
    lengthslst = []
    while i < len(v):
        v[i] = len(v[i])
        lengthslst.append(v[i])
        i = i + 1
    return lengthslst

print(lengths(["abc", "ab", "a"]))

print("-----------------------------------------------------------------------------------------------")
print("Opgave 5")
print("in_unit_circle")
def in_unit_circle(v):
    if len(v) == 0:
        raise ValueError("List is empty")
    i = 0
    in_unit_circle_lst = []
    while i < len(v):
        if sqrt(v[i][0]*v[i][0] + v[i][1]*v[i][1]) < 1:
            in_unit_circle_lst.append(True)
        else:   
            in_unit_circle_lst.append(False)
        
        i = i + 1
    return in_unit_circle_lst

print(in_unit_circle([(0, 0), (1, 1), (0.5, 0.5)]))
    
print("-----------------------------------------------------------------------------------------------")
print("Opgave 6")
print("Lambda 1-5")
def lambda_func(v, f):
    if len(v) == 0:
        raise ValueError("List is empty")
    i = 0
    lambda_lst = []
    while i < len(v):
        v[i] = f(v[i])
        lambda_lst.append(v[i])
        i = i + 1
    return lambda_lst

print(lambda_func([5, 12, 4], (lambda x: x + 1)))
print(lambda_func([5, 12, 4], (lambda x: x * 2)))
print(lambda_func([5, 12, 4], (lambda x: x / 2)))
print(lambda_func([5, 12, 4], (lambda x: x ** 2)))
print(lambda_func(["test", "okkk", "ffff"], (lambda x: len(x))))


# Decrement
print("-----------------------------------------------------------------------------------------------")
print("Opgave 7")
print("Decrement")
def decrement(v):
    if len(v) == 0:
        raise ValueError("List is empty")
    i = 0
    newlst = []
    while i < len(v):
        v[i] = v[i] - 1
        newlst.append(v[i])
        i = i + 1    
    return newlst
print(decrement([1, 2, 3]))

#Danish vat
print("-----------------------------------------------------------------------------------------------")
print("Danish vat")
def danish_vat(v):
    if len(v) == 0:
        raise ValueError("List is empty")
    i = 0
    newlst = []
    while i < len(v):
        v[i] = v[i] * 1.25
        newlst.append(v[i])
        i = i + 1    
    return newlst
print(danish_vat([1, 2, 3]))

#Negate
print("-----------------------------------------------------------------------------------------------")
print("Opgave 8")
print("Negate")
def negate (v):
    if len(v) == 0:
        raise ValueError("List is empty")
    i = 0
    newlst = []
    while i < len(v):
        if v[i] == True:
            newlst.append(False)
        else:
            newlst.append(True)
        i = i + 1    
    return newlst

print(negate([True, False, False]))

print("-----------------------------------------------------------------------------------------------")
print("Opgave 10")
print("Lambda 7-9")
def lambda_func(v, f):
    if len(v) == 0:
        raise ValueError("List is empty")
    i = 0
    lambda_lst = []
    while i < len(v):
        v[i] = f(v[i])
        lambda_lst.append(v[i])
        i = i + 1
    return lambda_lst

print(lambda_func([5, 12, 4], (lambda x: x - 1)))
print(lambda_func([5, 12, 4], (lambda x: x * 2)))
print(lambda_func([5, 12, 4], (lambda x: x / 2)))
print(lambda_func([5, 12, 4], (lambda x: x ** 2)))
