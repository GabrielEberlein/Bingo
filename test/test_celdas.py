from src import bingo

_carton = bingo.newCarton()


def test_15celdasOcupadas():
    assert bingo.celdasOcupadasCarton(_carton) == 15

def test_cartonDe3x9():
    assert bingo.cartonDe3x9(_carton)

def test_columnasCon1CeldaOcupada():
    assert bingo.columnasCon1CeldaOcupada(_carton) == 3

def test_menosDe3CeldasPorColumna():
    assert bingo.menosDe3CeldasPorColumna(_carton) == 0

def test_columnasOcupadas():
    assert bingo.columnasOcupadas(_carton) == 9

def test_celdasConValoresValidos():
    assert bingo.valoresValidos(_carton) == 15

def test_celdaInferior():
    assert bingo.celdaInferior(_carton) == 9

def test_celdaDerecha():
    assert bingo.celdaDerecha(_carton) == 27

def test_celdaRepetida():
    assert bingo.celdasDiferentes(_carton) == 15

def test_5CeldasPorFila():
    assert bingo.filasCon5Celdas(_carton) == 3

def test_masDe2CeldasOcupadasConsecutivas():
    assert bingo.celdasOcupadasConsecutivas(_carton) == 0

def test_masDe2CeldasVaciasConsecutivas():
    assert bingo.celdasVaciasConsecutivas(_carton) == 0