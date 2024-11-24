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

def generar_coo_desde_archivo(archivo):
    """
    Genera la representación COO de una matriz cargada desde un archivo.

    Args:
        archivo (str): Ruta del archivo que contiene la matriz.

    Returns:
        dict: Representación en formato COO con claves:
            - 'valores': Lista de valores distintos de cero.
            - 'filas': Lista de índices de fila de los valores.
            - 'columnas': Lista de índices de columna de los valores.
    """
    matriz = cargar_matriz(archivo)
    return generar_coo(matriz)

def generar_coo(matriz):
    """
    Genera la representación COO de una matriz dispersa.

    Args:
        matriz (list[list[int]]): Matriz dispersa representada como lista de listas.

    Returns:
        dict: Representación en formato COO con claves:
            - 'valores': Lista de valores distintos de cero.
            - 'filas': Lista de índices de fila de los valores.
            - 'columnas': Lista de índices de columna de los valores.
    """
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


def matriz_desde_coo(coo):
    """
    Reconstruye una matriz dispersa a partir de su representación COO.

    Args:
        coo (dict): Representación COO con claves:
            - 'valores': Lista de valores distintos de cero.
            - 'filas': Lista de índices de fila.
            - 'columnas': Lista de índices de columna.

    Returns:
        list[list[int]]: Matriz dispersa reconstruida.
    """
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
