__author__ = 'exak'


def hash_func(ignored, item):
    print('test', item)
    return 1


class Loader:
    hash_fun = hash_func

    item_hashes = []

    def __init__(self, items):
        self.items = items
        self.load()

    def load(self):
        self.item_hashes = list(map(self.hash_fun, self.items))

    def __len__(self):
        return len(self.item_hashes)
