from bloom_kata import BloomFilter

__author__ = 'exak'

sut = BloomFilter.BloomFilter(10, 1)


def test_init():
    assert sut is not None


def test_empty_filters_have_empty_array():
    assert sut.array.all(0) is True


def test_given_an_object_it_changes_the_state_of_the_filter():
    sut.load("hello")
    assert sut.array.any(1) is True

