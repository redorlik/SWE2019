import pytest
from rle import encode,decode,MyException
from hypothesis import given
from hypothesis.strategies import text

def test_rle():
    assert encode('kkk') == '3k'

def test_encode2():
    assert encode('kkkkkkoooo') == '6k4o'

def test_empty():
    assert encode('') == ''

def test_emoji():
    assert encode('😇😇😇😇😇😇😇😇😍😍😍😍😍😍😍') =='8😇7😍'

def test_None():
    with pytest.raises(MyException) as info:
        encode(None) == ''

def test_space():
    assert encode('kkk   ooo') == '3k3 3o'

def test_digit():
    assert encode('www111111qqq') == '3w613q'

def test_escape():
    assert encode('\\'*4) == '4\\'

def test_int():
    with pytest.raises(MyException) as exc_info:
        encode(123)

def test_decode():
    assert decode('3b4,19 ') == 'bbb,,,,'+ ' '*19

@given(text())
def test_encode_decode(s):
    #s = '2222aaaaaaaaafffffuuuu9999'
    print(s)
    assert decode(encode(s)) == s
