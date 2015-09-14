__author__ = 'exak'
from bloom_kata import loader
import os

def test_load():
    assert loader.load() == 338781
