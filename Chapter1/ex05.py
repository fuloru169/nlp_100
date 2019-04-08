def n_gram(target,num):
    result_list = []
    for i in range(0, len(target) - num + 1):
        result_list.append(target[i:(i + num)])
    return result_list

def test_n_gram():
    assert n_gram('I am an NLPer'.split(' '), 2) == \
    [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
    assert n_gram('I am an NLPer', 2) == \
    ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
