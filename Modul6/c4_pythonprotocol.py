class Dictionary:
    def __init__(self):

        self._v = [] 
    
    def __setitem__(self, key, value):

        self._v.append((key, value))

    def __str__(self):
        return str(self._v)
    
    def __repr__(self):
        return f"{self._v}"
 
    def __getitem__(self, key):

        i = 0
        while i < len(self._v):
            k, v = self._v[i]
            if k == key:
                return v
            i += 1
        return None
    
    def find(self, key):

        i = 0
        while i < len(self._v):
            if self._v[i][0] == key:
                return i
            i += 1
        return -1


    def __contains__(self, key):
        i = 0
        while i < len(self._v):
            k, v = self._v[i]  
            if k == key:      
                return True
            i += 1
        return False

    def __delitem__(self, key):

        i = 0
        while i < len(self._v):
            if self._v[i][0] == key:
                del self._v[i]
                return  
            i += 1

    def __len__(self):

        return len(self._v)


if __name__ == '__main__':
    
    d0 = Dictionary()
    d1 = Dictionary()
    d2 = Dictionary()
    d3 = Dictionary()
    d4 = Dictionary()

    d1['a'] = 7
    d2['dk'] = 207
    d2['no'] = 208
    d3['dk'] = 307
    d3['se'] = 309
    d3['fi'] = 310
    d4['dk'] = 307
    d4['se'] = 309

print(d0['a']) # None
print(d1['a']) # 7

print('a' in d0) # False
print('a' in d1) # True

print('fi' in d3) # True
del d3['fi']
print('fi' in d3) # False

if d0:
    print('The dictionary is empty')     # The dictionary is empty
else:
    print('The dictionary is non-empty')

print(len(d0)) # 0
print(len(d1)) # 1
print(len(d2)) # 2

print(d0)       # {} 
print(d1)       # {'a': 7}
print([d2, d3]) # [{'dk': 207, 'no': 208}, {'dk': 307, 'se': 309}]

for key in d2:
    print(key) # dk, no