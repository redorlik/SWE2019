
from rle import rle

def test_rle():
    assert rle('kkk') == '3k'

def test_rle2():
    assert rle('kkkkkkoooo') == '6k4o'

def test_empty():
    assert rle('') == ''
