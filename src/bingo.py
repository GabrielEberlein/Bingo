def carton():
    carton=(
    (0,0,27,36,0,52,62,0,80),
    (0,11,0,37,41,0,0,75,88),
    (3,12,0,0,48,0,65,76,0)
    )
    return carton


def contarCeldasOcupadas(arr):
    contador = 0
    for celdas in arr:
        if celdas > 0:
            contador+=1

    return contador


def columnasOcupadas(_carton):
    columnasValidas = 0
    for indiceColumna in range(9):
        if _carton[0][indiceColumna] or _carton[1][indiceColumna] or _carton[2][indiceColumna]:
            columnasValidas+=1

    return columnasValidas

def menosDe3CeldasPorColumna(_carton):
    columnasInvalidas=0
    for columnas in range(9):
        if(_carton[0][columnas] & _carton[1][columnas] & _carton[2][columnas]):
            columnasInvalidas+=1
    return columnasInvalidas

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

def celdaDerecha(_carton):
    celdasValidas=3
    for indiceFila in range(3):
        for indiceColumna in range(8):
            if _carton[indiceFila][indiceColumna] and _carton[indiceFila][indiceColumna+1]:
                if _carton[indiceFila][indiceColumna] < _carton[indiceFila][indiceColumna+1]:
                    celdasValidas+=1
            else:
                celdasValidas+=1

    return celdasValidas

def celdasDiferentes(_carton):
    valoresUnicos=0
    for indiceFila in range(3):
        valoresUnicos+=len(set(_carton[indiceFila]))-1

    return valoresUnicos

def valoresValidos(_carton):
    celdasValidas = 0
    for fila in range(3):
        for celda in range(9):
            celdaActual = _carton[fila][celda]
            if celdaActual >= 1 and celdaActual <= 90:
                celdasValidas+=1

    return celdasValidas

def celdasOcupadasConsecutivas(_carton):
    celdasConsecutivas = 0
    for filas in range(3):
        fila = _carton[filas]
        for celda in range(7):
            if fila[celda] and fila[celda+1] and fila[celda+2]:
                celdasConsecutivas+=1
    
    return celdasConsecutivas

def celdasVaciasConsecutivas(_carton):
    celdasConsecutivas = 0
    for filas in range(3):
        fila = _carton[filas]
        for celda in range(7):
            if not(fila[celda] or fila[celda+1] or fila[celda+2]):
                celdasConsecutivas+=1
    
    return celdasConsecutivas
