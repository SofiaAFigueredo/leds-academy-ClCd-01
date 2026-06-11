from src.operations import adicionar, subtrair

def test_numeros_positivos():
    assert adicionar(2, 3) == 5

def test_numeros_negativos():
    assert adicionar(-1, -1) == -2

def test_subtrair_numeros_positivos():
    assert subtrair(5, 3) == 2

def test_subtrair_numeros_negativos():
    assert subtrair(-1, -1) == 0