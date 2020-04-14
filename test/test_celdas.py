from src.bingo import carton

def test_cantidadDeCeldas():
    _carton = carton()
    contador = 0
    for filas in _carton:
        for celdas in filas:
            contador+=celdas

    assert contador == 15
