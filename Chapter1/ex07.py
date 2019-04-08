def template_text(x, y, z):
    return f'{x}時の{y}は{z}'

def test_template_text():
    assert template_text(12, '気温', 22.4) == '12時の気温は22.4'

print(template_text(12, '気温', 22.4))
