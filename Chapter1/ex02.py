def cross_concat(target1,target2):
    return ''.join([i + j for i,j in zip(target1,target2)])

def test_cross_concat():
    assert cross_concat('パトカー','タクシー') == 'パタトクカシーー'
