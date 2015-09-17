from bloom_kata import BloomFilter

__author__ = 'exak'


def test_load():
    sut = BloomFilter.BloomFilter(10, 1)
    assert sut is not None
