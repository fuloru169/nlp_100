import random

def typoglycemia(text):
    random.seed(169)
    return ' '.join([t if len(t) <= 4 else t[0] + ''.join(random.sample([c for c in t[1:-1]],len(t[1:-1]))) + t[-1] for t in text.split(' ')])

def test_typoglycemia():
    assert typoglycemia('I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind .') == 'I clnu\'odt bvileee that I cloud aactlluy ureasndntd what I was rieadng : the pmoeneahnl poewr of the hmaun mind .'
