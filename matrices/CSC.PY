def generar_csc(matriz):
    valores = []
    filas = []
    p_columnas = [0]  # Siempre empieza en 0

    num_columnas = len(matriz[0]) if matriz else 0
    for j in range(num_columnas):
        count = 0  # Contador de valores no cero en la columna actual
        for i, fila in enumerate(matriz):
            if fila[j] != 0:
                valores.append(fila[j])
                filas.append(i)
                count += 1
        p_columnas.append(p_columnas[-1] + count)

    return {
        "valores": valores,
        "filas": filas,
        "p_columnas": p_columnas
    }

def generar_csc_desde_archivo(archivo):

    matriz = cargar_matriz(archivo)
    return generar_csc(matriz)

def cargar_matriz(archivo):
   
    matriz = []
    with open(archivo, 'r') as f:
        for linea in f:
            fila = list(map(int, linea.strip().split()))
            matriz.append(fila)
    return matriz


def matriz_desde_csc(csc):

    p_columnas = csc["p_columnas"]
    filas = csc["filas"]
    valores = csc["valores"]

    num_columnas = len(p_columnas) - 1
    num_filas = max(filas) + 1

    matriz = [[0 for _ in range(num_columnas)] for _ in range(num_filas)]

    for j in range(num_columnas):
        start = p_columnas[j]
        end = p_columnas[j + 1]
        for i in range(start, end):
            matriz[filas[i]][j] = valores[i]

    return matriz


def cargar_representacion_csc(archivo):
    with open(archivo, 'r') as f:
        valores = f.readline().strip().split(":")[1].strip()[1:-1]
        valores = list(map(int, valores.replace(",", " ").split()))
        filas = f.readline().strip().split(":")[1].strip()[1:-1]
        filas = list(map(int, filas.replace(",", " ").split()))
        p_columnas = f.readline().strip().split(":")[1].strip()[1:-1]
        p_columnas = list(map(int, p_columnas.replace(",", " ").split()))
    return {"valores": valores, "filas": filas, "p_columnas": p_columnas}


def reconstruir_matriz_csc(representacion):
    n = len(representacion["p_columnas"]) - 1
    m = max(representacion["filas"]) + 1
    matriz = [[0] * n for _ in range(m)]
    for columna in range(n):
        inicio = representacion["p_columnas"][columna]
        fin = representacion["p_columnas"][columna + 1]
        for idx in range(inicio, fin):
            matriz[representacion["filas"][idx]][columna] = representacion["valores"][idx]
    return matriz