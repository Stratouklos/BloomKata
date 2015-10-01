__author__ = 'exak'
from bitstring import BitArray
from hashlib import md5


class BloomFilter:
    def __init__(self, size, hash_count):
        self.array = BitArray(length=size)
        self.hash_list = [md5() in range(hash_count)]

    def load(self, items):
        for item in items:
            self.array.set(1, [h.real for h in self.hash_list])

    def __contains__(self, item):
        a = [h.real for h in self.hash_list]
        return self.array[a]
