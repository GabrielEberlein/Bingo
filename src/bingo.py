import random
import math

def carton():
    carton=(
    (0,0,27,36,0,52,62,0,80),
    (0,11,0,37,41,0,0,75,88),
    (3,12,0,0,48,0,65,76,0)
    )
    return carton

def intentoCarton():
    contador = 0

    carton = [
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0]
    ]
    numerosCarton = 0

    while numerosCarton < 15:
      contador+=1
      if contador == 50:
        return intentoCarton()
      
      numero = random.randint(1, 90)
      columna = int(math.floor(numero / 10))

      if columna == 9:
        columna = 8
      huecos = 0
      for i in range(3):
        if carton[i][columna] == 0:
          huecos+=1
        
        if carton[i][columna] == numero:
          huecos = 0
          break
        
      if (huecos < 2):
        continue

      fila = 0
      for j in range(3):
        huecos = 0
        for i in range(9):
          if carton[fila][i] == 0:
            huecos+=1

        if huecos < 5 or carton[fila][columna] != 0: 
          fila+=1
        else:
          break

      if fila == 3:
        continue

      carton[fila][columna] = numero
      numerosCarton+=1
      contador = 0

    for x in range(9):
      huecos = 0
      for y in range(3):
        if carton[y][x] == 0:
            huecos+=1
      if huecos == 3:
        return intentoCarton()

    return carton

def newCarton():
    while 1:
        carton=intentoCarton()
        if(
            columnasOcupadas(carton) == 9 and
            celdasOcupadasCarton(carton) == 15 and
            cartonDe3x9(carton) and
            columnasCon1CeldaOcupada(carton) == 3 and
            menosDe3CeldasPorColumna(carton) == 0 and
            valoresValidos(carton) == 15 and
            celdaInferior(carton) == 27 and
            celdaDerecha(carton) == 27 and
            celdasDiferentes(carton) == 15 and
            filasCon5Celdas(carton) == 3 and
            celdasOcupadasConsecutivas(carton) == 0 and
            celdasVaciasConsecutivas(carton) == 0
        ):
            break
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

def celdasOcupadasCarton(_carton):
    celdasOcupadas = 0
    for filas in _carton:
        celdasOcupadas += contarCeldasOcupadas(filas) 
    return celdasOcupadas

def cartonDe3x9(_carton):
    if(len(_carton[0])==len(_carton[1]) and len(_carton[1])==len(_carton[2])):
        return len(_carton) * len(_carton[0]) == 27
    else:
        return False

def columnasCon1CeldaOcupada(_carton):
    columnasValidas = 0
    for columnas in range(9):
        columna = (_carton[0][columnas],_carton[1][columnas],_carton[2][columnas])
        if(contarCeldasOcupadas(columna) == 1):
            columnasValidas+=1
    
    return columnasValidas

def menosDe3CeldasPorColumna(_carton):
    columnasInvalidas=0
    for columnas in range(9):
        if(_carton[0][columnas] and _carton[1][columnas] and _carton[2][columnas]):
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
            if celdaActual >0 and celdaActual >= (10*celda) and celdaActual <= (10*(celda+1)-1):
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

def filasCon5Celdas(_carton):
    celdasOcupadas = 0
    filasValidas = 0
    for filas in _carton:
        celdasOcupadas = contarCeldasOcupadas(filas)
        if(celdasOcupadas==5):
            filasValidas+=1
    
    return filasValidas