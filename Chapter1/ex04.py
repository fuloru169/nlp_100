def element_map(target):
    SINGLE_ALPHABET_ELEMENT_LIST = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    count = 1
    element_dict = {}
    for element in target.split():
        if (count in SINGLE_ALPHABET_ELEMENT_LIST):
            element_dict.setdefault(element[0:1], count)
        else:
            element_dict.setdefault(element[0:2], count)
        count += 1
    return element_dict

def test_element_map():
    assert element_map('Hi He Lied Because Boron Could Not Oxidize Fluorine. \
    New Nations Might Also Sign Peace Security Clause. Arthur King Can.') == \
    {'H':1, 'He':2, 'Li':3, 'Be':4, 'B':5, 'C':6, 'N':7, 'O':8, 'F':9, \
    'Ne':10, 'Na':11, 'Mi':12, 'Al':13, 'Si':14, 'P':15, 'S':16, 'Cl':17, \
    'Ar':18, 'K':19, 'Ca':20}
