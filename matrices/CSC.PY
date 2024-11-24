def generar_csc(matriz):
    """
    Genera la representación CSC de una matriz dispersa.

    Args:
        matriz (list[list[int]]): Matriz dispersa representada como lista de listas.

    Returns:
        dict: Representación en formato CSC con claves:
            - 'valores': Lista de valores distintos de cero.
            - 'filas': Lista de índices de fila de los valores.
            - 'p_columnas': Lista de posiciones donde inician los valores de cada columna.
    """
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
    """
    Genera la representación CSC de una matriz cargada desde un archivo.

    Args:
        archivo (str): Ruta del archivo que contiene la matriz.

    Returns:
        dict: Representación en formato CSC.
    """
    matriz = cargar_matriz(archivo)
    return generar_csc(matriz)

def cargar_matriz(archivo):
    """
    Carga una matriz desde un archivo .txt.

    Args:
        archivo (str): Ruta del archivo que contiene la matriz.

    Returns:
        list[list[int]]: Matriz dispersa representada como lista de listas.
    """
    matriz = []
    with open(archivo, 'r') as f:
        for linea in f:
            fila = list(map(int, linea.strip().split()))
            matriz.append(fila)
    return matriz


def matriz_desde_csc(csc):
    """
    Reconstruye una matriz dispersa a partir de su representación CSC.

    Args:
        csc (dict): Representación CSC con claves:
            - 'valores': Lista de valores distintos de cero.
            - 'filas': Lista de índices de fila.
            - 'p_columnas': Lista de posiciones donde inician los valores por columna.

    Returns:
        list[list[int]]: Matriz dispersa reconstruida.
    """
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
