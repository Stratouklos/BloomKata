from bloom_kata import ObjectIndexer
from hashlib import md5

__author__ = 'exak'

f = md5()

sut = ObjectIndexer.ObjectIndexer(256)


def test_init():
    assert sut is not None


def test_an_object_returns_an_index():
    assert sut.get_index("hello") == 1236


def test_indexing_an_object_twice_returns_the_same_index():
    assert sut.get_index("hello") == sut.get_index("hello")
