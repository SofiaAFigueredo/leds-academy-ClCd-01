from calculadora import somar, subtrair

def test_somar():
    # Aqui dizemos: "Eu espero que somar 2 + 3 seja igual a 5"
    assert somar(2, 3) == 5

def test_subtrair():
    # Aqui dizemos: "Eu espero que subtrair 5 - 2 seja igual a 3"
    assert subtrair(5, 2) == 3
    