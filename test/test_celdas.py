from src import bingo

_carton = bingo.carton()


def test_15celdasOcupadas():
    celdasOcupadas = 0
    for filas in _carton:
        celdasOcupadas += bingo.contarCeldasOcupadas(filas) 
    assert celdasOcupadas==15

def test_cartonDe3x9():
    if(len(_carton[0])==len(_carton[1]) and len(_carton[1])==len(_carton[2])):
        assert len(_carton) * len(_carton[0]) == 27
    else:
        assert False

def test_columnasCon1CeldaOcupada():
    columnasValidas = 0
    for columnas in range(9):
        columna = (_carton[0][columnas],_carton[1][columnas],_carton[2][columnas])
        if(bingo.contarCeldasOcupadas(columna) == 1):
            columnasValidas+=1
    
    assert columnasValidas == 3

def test_menosDe3CeldasPorColumna():
    assert bingo.menosDe3CeldasPorColumna(_carton) == 0

def test_columnasOcupadas():
    assert bingo.columnasOcupadas(_carton) == 9

def test_celdasEntre1y90():
    assert bingo.valoresValidos(_carton) == 15

def test_celdaInferior():
    assert bingo.celdaInferior(_carton) == 27

def test_celdaDerecha():
    assert bingo.celdaDerecha(_carton) == 27

def test_celdaRepetida():
    assert bingo.celdasDiferentes(_carton) == 15

def test_5CeldasPorFila():
    celdasOcupadas = 0
    filasValidas = 0
    for filas in _carton:
        celdasOcupadas = bingo.contarCeldasOcupadas(filas)
        if(celdasOcupadas==5):
            filasValidas+=1
    
    assert filasValidas == 3

def test_masDe2CeldasOcupadasConsecutivas():
    assert bingo.celdasOcupadasConsecutivas(_carton) == 0

def test_masDe2CeldasVaciasConsecutivas():
    assert bingo.celdasVaciasConsecutivas(_carton) == 0