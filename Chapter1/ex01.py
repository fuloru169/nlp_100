def odd_concat(str):
    return str[::2]

def test_odd_concat():
    assert odd_concat('パタトクカシー') == 'パトカー'
