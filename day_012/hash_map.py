import ipdb

class HashMap:
    def __init__(self, size=64):
        self.size = size
        self.hash_list = [[] for index in range(1, self.size)]

    def display(self):
        return print(self.hash_list)

    def add(self, key, value):
        index = self._hash(value)
        self.hash_list[index].append({key:value})

    def _hash(self, value):
        sum_of_ascii_codes = 0
        for letter in value:
           sum_of_ascii_codes += ord(letter)
        return sum_of_ascii_codes % self.size


hashmap = HashMap()
hashmap.add('name','raymond')
hashmap.add('name','gabriel')
hashmap.add('name','gabriel')
hashmap.display()
