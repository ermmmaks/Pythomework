from src.hamming import encode, decode

def test_encode():
    assert encode('1011') == '0110011'
    assert encode('11010110') == '001010100110'

def test_decode():
    encoded_data4 = '0110011'
    assert decode(encoded_data4) == -1

    encoded_data8 = '001010100110'
    assert decode(encoded_data8) == -1