def generar_csr(matriz):
    """
    Genera la representación CSR de una matriz dispersa.

    Args:
        matriz (list[list[int]]): Matriz dispersa representada como lista de listas.

    Returns:
        dict: Representación en formato CSR con claves:
            - 'valores': Lista de valores distintos de cero.
            - 'columnas': Lista de índices de columna de los valores.
            - 'p_filas': Lista de posiciones donde inician los valores de cada fila.
    """
    valores = []
    columnas = []
    p_filas = [0]  # Siempre empieza en 0

    for fila in matriz:
        count = 0  # Contador de valores no cero en la fila actual
        for j, valor in enumerate(fila):
            if valor != 0:
                valores.append(valor)
                columnas.append(j)
                count += 1
        p_filas.append(p_filas[-1] + count)

    return {
        "valores": valores,
        "columnas": columnas,
        "p_filas": p_filas
    }

def generar_csr_desde_archivo(archivo):
    """
    Genera la representación CSR de una matriz cargada desde un archivo.

    Args:
        archivo (str): Ruta del archivo que contiene la matriz.

    Returns:
        dict: Representación en formato CSR.
    """
    matriz = cargar_matriz(archivo)
    return generar_csr(matriz)

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


def matriz_desde_csr(csr):
    """
    Reconstruye una matriz dispersa a partir de su representación CSR.

    Args:
        csr (dict): Representación CSR con claves:
            - 'valores': Lista de valores distintos de cero.
            - 'columnas': Lista de índices de columna.
            - 'p_filas': Lista de posiciones donde inician los valores por fila.

    Returns:
        list[list[int]]: Matriz dispersa reconstruida.
    """
    p_filas = csr["p_filas"]
    columnas = csr["columnas"]
    valores = csr["valores"]

    num_filas = len(p_filas) - 1
    num_columnas = max(columnas) + 1

    matriz = [[0 for _ in range(num_columnas)] for _ in range(num_filas)]

    for i in range(num_filas):
        start = p_filas[i]
        end = p_filas[i + 1]
        for j in range(start, end):
            matriz[i][columnas[j]] = valores[j]

    return matriz
