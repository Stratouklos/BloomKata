__author__ = 'exak'

import pytest
from bloom_kata import scaler
from hashlib import sha256


def test_small_scales_throw_error():
    with pytest.raises(ValueError):
        scaler.scale_down([], 255)


def test_empty_digit_array_throws_error():
    with pytest.raises(TypeError):
        scaler.scale_down(None, 256)


def test_get_top_scaled_hash():
    assert scaler.scale_down('ff', 256) == 255


def test_hash_at_higher_scale():
    m = sha256()
    m.update('adfa21341231sdasfc'.encode('utf-8'))
    assert 256 < scaler.scale_down(m.hexdigest(), 65535) < 65535
