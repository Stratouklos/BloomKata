__author__ = 'exak'


class BloomFilter:
    filter = bytearray

    def __init__(self, size, hashes_count):
        self.hashes_count = hashes_count
        self.size = size

    def insert(self, item):
        print(item)
