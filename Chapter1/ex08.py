def cipher(text):
    return ''.join([chr(219 - ord(w)) if w.islower() else w for w in text])

def test_cipher():
    assert cipher('I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind .') == 'I xlfowm\'g yvorvev gszg I xlfow zxgfzoob fmwvihgzmw dszg I dzh ivzwrmt : gsv ksvmlnvmzo kldvi lu gsv sfnzm nrmw .'
    assert cipher('I xlfowm\'g yvorvev gszg I xlfow zxgfzoob fmwvihgzmw dszg I dzh ivzwrmt : gsv ksvmlnvmzo kldvi lu gsv sfnzm nrmw .') == 'I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
