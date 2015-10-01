from bloom_kata import BloomFilter

__author__ = 'exak'

sut = BloomFilter.BloomFilter(10, 1)


def test_init():
    assert sut is not None

# def test_positive_result():
#     sut.load("hello")
#     assert "hello" in sut
#
#
# def test_negative_result():
#     assert "booga" not in sut
