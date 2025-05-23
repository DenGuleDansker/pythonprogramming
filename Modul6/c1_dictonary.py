class Dictionary:

    def __init__(self):

        self._v = [] 

    def add_entry(self, key, value):

        self._v.append((key, value))

    def lookup_entry(self, key):

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


    def contains_key(self, key):

        i = 0
        while i < len(self._v):
            k = self._v[i]
            if k == key:
                return True
            i += 1
        return False

    def delete_entry(self, key):

        i = 0
        while i < len(self._v):
            if self._v[i][0] == key:
                del self._v[i]
                return  
            i += 1

    def size(self):

        return len(self._v)


if __name__ == '__main__':

    dictionary = Dictionary()
    dictionary.add_entry("August", "Arbejder hos Wexo")
    dictionary.add_entry("Chi Linh", "Arbejder hos Wexo")

    
    print(dictionary.lookup_entry("August"))
    print(dictionary.lookup_entry("Chi Linh"))
    print(f"Er August i mit dictionary : {dictionary.contains_key("August")}")
    print(f"Hvad er længden af min dictonary {dictionary.size()}")
    print(f"August bliver nu slettet i systemet : {dictionary.delete_entry("August")}")

    print(f"Er August her stadig? : {dictionary.contains_key("August")}")

