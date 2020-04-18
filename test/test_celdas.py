from src.bingo import carton

def test_cantidadDeCeldas():
    _carton = carton()
    contador = 0
    for filas in _carton:
        for celdas in filas:
            contador+=celdas

    assert contador == 15

def test_columnasVacias():
    _carton = carton()
    columnasValidas = 0
    for indiceColumna in range(9):
        if _carton[0][indiceColumna] or _carton[1][indiceColumna] or _carton[2][indiceColumna]:
            columnasValidas+=1

    assert columnasValidas == 9

def test_filasVacias():
    _carton = carton()
    filasValidas = 0
    for filas in _carton:
        for celdas in filas:
            if celdas:
                filasValidas+=1
                break
    
    assert filasValidas == 3