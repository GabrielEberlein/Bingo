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


