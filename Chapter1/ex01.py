def odd_concat(target):
    return target[::2]

def test_odd_concat():
    assert odd_concat('パタトクカシー') == 'パトカー'
