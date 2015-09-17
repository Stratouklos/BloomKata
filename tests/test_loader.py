from bloom_kata import loader

__author__ = 'exak'


def test_load():
    sut = loader.Loader(["a", "b", "c"])
    assert len(sut) == 3
