__author__ = 'exak'


class Loader:

    def __init__(self, items):
        self.item_hashes = list(map(hash, items))

    def __len__(self):
        return len(self.item_hashes)
