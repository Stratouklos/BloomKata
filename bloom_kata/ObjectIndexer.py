from bloom_kata import scaler
import hashlib

__author__ = 'exak'


class ObjectIndexer:
    def __init__(self, size, hashName='md5'):
        self.hashName = hashName
        self.size = size

    def get_index(self, item):
        function = hashlib.new(self.hashName, item.encode('UTF-8'))
        hexhash = function.hexdigest()
        return scaler.scale_down(hexhash, self.size)
