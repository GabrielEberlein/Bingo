def carton():
    carton=(
    (1,0,1,0,1,0,1,1,1),
    (0,1,0,1,0,1,0,1,0),
    (1,0,1,0,1,0,1,0,1)
    )
    return carton

def contarCeldasOcupadas(_carton):
    contador = 0
    for filas in _carton:
        for celdas in filas:
            if celdas > 0:
                contador+=1

    return contador

def columnasOcupadas(_carton):
    columnasValidas = 0
    for indiceColumna in range(9):
        if _carton[0][indiceColumna] or _carton[1][indiceColumna] or _carton[2][indiceColumna]:
            columnasValidas+=1

    return columnasValidas

def filasOcupadas(_carton):
    filasValidas = 0
    for filas in _carton:
        for celdas in filas:
            if celdas:
                filasValidas+=1
                break
    
    return filasValidas

def celdaInferior(_carton):
    celdasValidas=9
    for indiceFila in range(2):
        for indiceColumna in range(9):
            if _carton[indiceFila][indiceColumna] and _carton[indiceFila+1][indiceColumna]:
                if _carton[indiceFila][indiceColumna] < _carton[indiceFila+1][indiceColumna]:
                    celdasValidas+=1
            else:
                celdasValidas+=1

    return celdasValidas

def valoresValidos(_carton):
    celdasValidas = 0
    for fila in range(3):
        for celda in range(9):
            celdaActual = _carton[fila][celda]
            if celdaActual >= 1 and celdaActual <= 90:
                celdasValidas+=1

    return celdasValidas
