from utils.utils import descontaNota

def test_desconto():
    assert descontaNota(8,30) == 5.6
    assert descontaNota(10,20) == 8.0
    assert descontaNota(7,25) == 5.25
    assert descontaNota(8.5,30) == 5.95
    assert descontaNota(6,20) == 4.8
