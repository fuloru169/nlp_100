import re

def count_words(target):
    return list(map(lambda x: len(x), re.sub('[,.]','',target).split()))

def test_count_words():
    assert count_words('Now I need a drink, \
    alcoholic of course, after the heavy lectures \
    involving quantum mechanics.') == \
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
