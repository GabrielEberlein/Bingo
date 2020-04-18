from src.bingo import carton

def contarCeldasOcupadas():
    _carton = carton()
    contador = 0
    for filas in _carton:
        for celdas in filas:
            contador+=celdas

    return contador

def test_masDe15Celdas():
    assert not(contarCeldasOcupadas()>15)

def test_menosDe15Celdas():
    assert not(contarCeldasOcupadas()<15)

def test_columnasVacias():
    _carton = carton()
    columnasValidas = 0
    for indiceColumna in range(9):
        if _carton[0][indiceColumna] or _carton[1][indiceColumna] or _carton[2][indiceColumna]:
            columnasValidas+=1

    assert columnasValidas == 9
