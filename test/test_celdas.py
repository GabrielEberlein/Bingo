from src import bingo

_carton = bingo.carton()


def test_masDe15Celdas():
    assert not(bingo.contarCeldasOcupadas(_carton)>15)

def test_menosDe15Celdas():
    assert not(bingo.contarCeldasOcupadas(_carton)<15)

def test_columnasOcupadas():
    assert bingo.columnasOcupadas(_carton) == 9

def test_filasOcupadas():
    assert bingo.filasOcupadas(_carton) == 3

def test_celdasEntre1y90():
    assert bingo.valoresValidos(_carton) == 15

def test_celdaInferior():
    assert bingo.celdaInferior(_carton) == 27

def test_celdaDerecha():
    assert bingo.celdaDerecha(_carton) == 27

def test_celdaRepetida():
    assert bingo.celdasDiferentes(_carton) == 15