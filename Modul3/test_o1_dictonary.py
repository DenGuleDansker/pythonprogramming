from o1_dictonary import invert

def test_invert():
    v = ['dk', 'se', 'no', 'gb']
    d = invert(v)
    
    assert d['dk'] == 0
    assert d['se'] == 1
    assert d['no'] == 2
    assert d['gb'] == 3
    assert len(d) == 4
    assert list(d.keys()) == v