def generar_csr(matriz):
   
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
 
    matriz = cargar_matriz(archivo)
    return generar_csr(matriz)

def cargar_matriz(archivo):
   
    matriz = []
    with open(archivo, 'r') as f:
        for linea in f:
            fila = list(map(int, linea.strip().split()))
            matriz.append(fila)
    return matriz


def matriz_desde_csr(csr):
   
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



def cargar_representacion_csr(archivo):
    with open(archivo, 'r') as f:
        valores = f.readline().strip().split(":")[1].strip()[1:-1]
        valores = list(map(int, valores.replace(",", " ").split()))
        columnas = f.readline().strip().split(":")[1].strip()[1:-1]
        columnas = list(map(int, columnas.replace(",", " ").split()))
        p_filas = f.readline().strip().split(":")[1].strip()[1:-1]
        p_filas = list(map(int, p_filas.replace(",", " ").split()))
    return {"valores": valores, "columnas": columnas, "p_filas": p_filas}




def reconstruir_matriz_csr(representacion):
    m = len(representacion["p_filas"]) - 1
    n = max(representacion["columnas"]) + 1
    matriz = [[0] * n for _ in range(m)]
    for fila in range(m):
        inicio = representacion["p_filas"][fila]
        fin = representacion["p_filas"][fila + 1]
        for idx in range(inicio, fin):
            matriz[fila][representacion["columnas"][idx]] = representacion["valores"][idx]
    return matriz