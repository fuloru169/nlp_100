def n_gram_set(x, y, target):
    result_list = []
    set_x = set(n_gram(x,2))
    set_y = set(n_gram(y,2))
    result_list.append(set_x)
    result_list.append(set_y)
    result_list.append(set_x | set_y)
    result_list.append(set_x & set_y)
    result_list.append(set_x - set_y)
    result_list.append(target in set_x)
    result_list.append(target in set_y)
    return result_list

def n_gram(target, num):
    result_list = []
    for i in range(0, len(target) - num + 1):
        result_list.append(target[i:(i + num)])
    return result_list

def test_n_gram_set():
    assert n_gram_set('paraparaparadise', 'paragraph', 'se') == [ \
    {'ar', 'se', 'di', 'is', 'pa', 'ap', 'ad', 'ra'}, \
    {'ar', 'gr', 'ph', 'ra', 'pa', 'ap', 'ag'}, \
    {'ar', 'gr', 'se', 'ph', 'di', 'is', 'pa', 'ap', 'ad', 'ra', 'ag'}, \
    {'ar', 'ap', 'pa', 'ra'}, \
    {'di', 'is', 'se', 'ad'}, \
    True, \
    False
    ]
