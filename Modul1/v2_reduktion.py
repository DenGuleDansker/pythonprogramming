
print("-----------------------------------------------------------------------------------------------")
print("Opgave 1")
print("sum_of")

def sum_of(v):
    if len(v) == 0:
        return 0
    i = 0
    sumlst = []
    while i < len(v):
        sumlst.append(v[i])
        i = i + 1
    return sum(sumlst)

print(sum_of([1, 2, 3]))

print("-----------------------------------------------------------------------------------------------")
print("Opgave 2")
print("prod_of")
def prod_of(v):
    if len(v) == 0:
        return 1
    i = 0
    prodlst = []
    while i < len(v):
        prodlst.append(v[i]*v[i])
        i = i + 1
    return sum(prodlst)
print(prod_of([1, 2, 3]))

print("-----------------------------------------------------------------------------------------------")
print("Opgave 3")
print("concat_of")
def concat_of(v):
    if len(v) == 0:
        return ""
    i = 0
    concatlst = ""
    while i < len(v):
        concatlst += v[i]
        i = i + 1
    return concatlst

print(concat_of(["h","e","ll"]))
