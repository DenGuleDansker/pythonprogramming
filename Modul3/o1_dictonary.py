d = { 'dk': 'Copenhagen', 'se': 'Stockholm', 'no': 'Oslo' }

print(len(d))  # 3
print(d['dk']) # Copenhagen
print(d['se']) # Stockholm
print(d['no']) # Oslo
print("--------------------------------------------")

print('gb' in d) # False
print('dk' in d) # True

print("--------------------------------------------")

print("If kommando")
country_code = 'gb'
if country_code in d:
  print('Capital of', country_code, 'is', d[country_code])
else:
  print('Capital of', country_code, 'is unknown')

print("--------------------------------------------")
print("get kommando")

country_code = 'gb'
print('Capital of', country_code, 'is', d.get(country_code, 'unknown'))

print("--------------------------------------------")
print("keys metode")

print(list(d.keys())) # ['dk', 'se', 'no']

print("--------------------------------------------")
print("Tilføje eller erstatte med tilordningskommando")
d['gb'] = 'London' # new entry added
d['dk'] = 'Viborg' # existing entry modified (true in medieval times, circa 1000-1500)
print("d['gb'] = 'London'")
print("d['dk'] = 'Viborg'")

print("--------------------------------------------")
print("fjerne et opslag med ordbogen d med en del-kommando")
print("del d['gb']")
del d['gb']

print("--------------------------------------------")
print("Pop som også returnerer den tilknyttede værdi, hvis nøglen ikke findes, returnerer pop default-værdien fra 2.parameter")
print("d.pop('gb', None)")
d.pop('gb', None)

print("--------------------------------------------")
print("invert funktion")

def invert(v):
    ordbog = {}
    #Tilordningskommando
    i = 0
    while i < len(v):
        ordbog[v[i]] = i 
        i += 1 
    return ordbog

v = ['dk', 'se', 'no', 'gb']
d = invert(v)

print(d)  