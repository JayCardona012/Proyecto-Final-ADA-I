def cargar_matriz(archivo):
    matriz = []
    with open(archivo, 'r') as f:
        for linea in f:
            fila = list(map(int, linea.strip().split()))
            matriz.append(fila)
    return matriz


def generar_coo(matriz):
    valores = []
    filas = []
    columnas = []

    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor != 0:
                valores.append(valor)
                filas.append(i)
                columnas.append(j)

    return {
        "valores": valores,
        "filas": filas,
        "columnas": columnas
    }


def generar_coo_desde_archivo(archivo):
   
    matriz = cargar_matriz(archivo)
    return generar_coo(matriz)




def matriz_desde_coo(coo):

    # Determinar las dimensiones de la matriz
    filas = coo["filas"]
    columnas = coo["columnas"]
    max_filas = max(filas) + 1
    max_columnas = max(columnas) + 1

    # Crear una matriz llena de ceros
    matriz = [[0 for _ in range(max_columnas)] for _ in range(max_filas)]

    # Rellenar la matriz con los valores no cero
    for valor, fila, columna in zip(coo["valores"], filas, columnas):
        matriz[fila][columna] = valor

    return matriz


def cargar_representacion_coo(archivo):
    with open(archivo, 'r') as f:
        valores = f.readline().strip().split(":")[1].strip()[1:-1]
        valores = list(map(int, valores.replace(",", " ").split()))
        filas = f.readline().strip().split(":")[1].strip()[1:-1]
        filas = list(map(int, filas.replace(",", " ").split()))
        columnas = f.readline().strip().split(":")[1].strip()[1:-1]
        columnas = list(map(int, columnas.replace(",", " ").split()))
    return {"valores": valores, "filas": filas, "columnas": columnas}


def reconstruir_matriz_coo(representacion):
    m = max(representacion["filas"]) + 1
    n = max(representacion["columnas"]) + 1
    matriz = [[0] * n for _ in range(m)]
    for valor, fila, columna in zip(representacion["valores"], representacion["filas"], representacion["columnas"]):
        matriz[fila][columna] = valor
    return matriz