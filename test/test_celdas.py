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