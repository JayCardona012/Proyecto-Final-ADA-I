from matrices.COO import generar_coo_desde_archivo
from matrices.CSR import generar_csr_desde_archivo
from matrices.CSC import generar_csc_desde_archivo
from operaciones.operaciones import obtener_elemento, seleccionar_formato


def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Obtener representación a partir de una matriz")
        print("2. Otras operaciones")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            menu_obtener_representacion()
        elif opcion == "2":
            menu_otras_operaciones()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


def menu_obtener_representacion():
    archivo_matriz = "entradaArchivos/matriz.txt"
    
    while True:
        print("\n--- Menú Representaciones ---")
        print("1. Formato COO")
        print("2. Formato CSR")
        print("3. Formato CSC")
        print("4. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            coo = generar_coo_desde_archivo(archivo_matriz)
            print("\nRepresentación COO:")
            print(coo)
        elif opcion == "2":
            csr = generar_csr_desde_archivo(archivo_matriz)
            print("\nRepresentación CSR:")
            print(csr)
        elif opcion == "3":
            csc = generar_csc_desde_archivo(archivo_matriz)
            print("\nRepresentación CSC:")
            print(csc)
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")


def menu_otras_operaciones():
    """
    Muestra el menú para realizar otras operaciones.
    """
    archivo_representacion = "entradaArchivos/representacion1.txt"
    archivo_salida = "entradaArchivos/representacionSalida.txt"
    
    while True:
        print("\n--- Menú Otras Operaciones ---")
        print("1. Obtener matriz a partir de una representación")
        print("2. Obtener elemento dados sus índices (i, j)")
        print("3. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            menu_obtener_matriz(archivo_representacion, archivo_salida)
        elif opcion == "2":
            formato = seleccionar_formato()
            if validar_representacion(archivo_representacion, formato):
                i = int(input("Ingrese el índice de la fila (i): "))
                j = int(input("Ingrese el índice de la columna (j): "))
                representacion = cargar_representacion(archivo_representacion, formato)
                try:
                    valor = obtener_elemento(representacion, formato, i, j)
                    print(f"El valor en la posición ({i}, {j}) es: {valor}")
                except IndexError as e:
                    print(f"Error: {e}")
            else:
                print("Error: El archivo no contiene una representación válida para el formato seleccionado.")
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Intente nuevamente.")


def menu_obtener_matriz(archivo_representacion, archivo_salida):
    while True:
        print("\n--- Reconstruir Matriz desde Representación ---")
        print("1. Representación COO")
        print("2. Representación CSR")
        print("3. Representación CSC")
        print("4. Volver al menú anterior")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            if validar_representacion(archivo_representacion, "COO"):
                coo = cargar_representacion_coo(archivo_representacion)
                matriz = reconstruir_matriz_coo(coo)
                guardar_matriz_en_archivo(matriz, archivo_salida)
                print("Matriz generada y guardada desde representación COO.")
            else:
                print("Error: La entrada no corresponde a una representación COO.")
        elif opcion == "2":
            if validar_representacion(archivo_representacion, "CSR"):
                csr = cargar_representacion_csr(archivo_representacion)
                matriz = reconstruir_matriz_csr(csr)
                guardar_matriz_en_archivo(matriz, archivo_salida)
                print("Matriz generada y guardada desde representación CSR.")
            else:
                print("Error: La entrada no corresponde a una representación CSR.")
        elif opcion == "3":
            if validar_representacion(archivo_representacion, "CSC"):
                csc = cargar_representacion_csc(archivo_representacion)
                matriz = reconstruir_matriz_csc(csc)
                guardar_matriz_en_archivo(matriz, archivo_salida)
                print("Matriz generada y guardada desde representación CSC.")
            else:
                print("Error: La entrada no corresponde a una representación CSC.")
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")


def validar_representacion(archivo, formato):
    """
    Valida que el archivo tenga la estructura correcta para la representación seleccionada.

    Args:
        archivo (str): Ruta del archivo a validar.
        formato (str): Formato esperado ("COO", "CSR", "CSC").

    Returns:
        bool: True si es válido, False en caso contrario.
    """
    try:
        with open(archivo, 'r') as f:
            contenido = f.readlines()
        
        if formato == "COO":
            valores = "valores" in contenido[0]
            filas = "filas" in contenido[1]
            columnas = "columnas" in contenido[2]
            return valores and filas and columnas
        elif formato == "CSR":
            valores = "valores" in contenido[0]
            columnas = "columnas" in contenido[1]
            p_filas = "p-filas" in contenido[2]
            return valores and columnas and p_filas
        elif formato == "CSC":
            valores = "valores" in contenido[0]
            filas = "filas" in contenido[1]
            p_columnas = "p-columnas" in contenido[2]
            return valores and filas and p_columnas
        return False
    except Exception as e:
        print(f"Error al validar la representación: {e}")
        return False




            

def guardar_matriz_en_archivo(matriz, archivo_salida):
    """
    Guarda una matriz dispersa en un archivo.

    Args:
        matriz (list[list[int]]): La matriz dispersa.
        archivo_salida (str): Ruta del archivo de salida.
    """
    with open(archivo_salida, 'w') as f:
        for fila in matriz:
            f.write(" ".join(map(str, fila)) + "\n")
    print(f"Matriz guardada en {archivo_salida}")

def cargar_representacion_coo(archivo):
    with open(archivo, 'r') as f:
        valores = f.readline().strip().split(":")[1].strip()[1:-1]
        valores = list(map(int, valores.replace(",", " ").split()))
        filas = f.readline().strip().split(":")[1].strip()[1:-1]
        filas = list(map(int, filas.replace(",", " ").split()))
        columnas = f.readline().strip().split(":")[1].strip()[1:-1]
        columnas = list(map(int, columnas.replace(",", " ").split()))
    return {"valores": valores, "filas": filas, "columnas": columnas}

def cargar_representacion_csr(archivo):
    with open(archivo, 'r') as f:
        valores = f.readline().strip().split(":")[1].strip()[1:-1]
        valores = list(map(int, valores.replace(",", " ").split()))
        columnas = f.readline().strip().split(":")[1].strip()[1:-1]
        columnas = list(map(int, columnas.replace(",", " ").split()))
        p_filas = f.readline().strip().split(":")[1].strip()[1:-1]
        p_filas = list(map(int, p_filas.replace(",", " ").split()))
    return {"valores": valores, "columnas": columnas, "p_filas": p_filas}

def cargar_representacion_csc(archivo):
    with open(archivo, 'r') as f:
        valores = f.readline().strip().split(":")[1].strip()[1:-1]
        valores = list(map(int, valores.replace(",", " ").split()))
        filas = f.readline().strip().split(":")[1].strip()[1:-1]
        filas = list(map(int, filas.replace(",", " ").split()))
        p_columnas = f.readline().strip().split(":")[1].strip()[1:-1]
        p_columnas = list(map(int, p_columnas.replace(",", " ").split()))
    return {"valores": valores, "filas": filas, "p_columnas": p_columnas}

def reconstruir_matriz_coo(representacion):
    m = max(representacion["filas"]) + 1
    n = max(representacion["columnas"]) + 1
    matriz = [[0] * n for _ in range(m)]
    for valor, fila, columna in zip(representacion["valores"], representacion["filas"], representacion["columnas"]):
        matriz[fila][columna] = valor
    return matriz

def reconstruir_matriz_csr(representacion):
    m = len(representacion["p-filas"]) - 1
    n = max(representacion["columnas"]) + 1
    matriz = [[0] * n for _ in range(m)]
    for fila in range(m):
        inicio = representacion["p-filas"][fila]
        fin = representacion["p-filas"][fila + 1]
        for idx in range(inicio, fin):
            matriz[fila][representacion["columnas"][idx]] = representacion["valores"][idx]
    return matriz

def reconstruir_matriz_csc(representacion):
    n = len(representacion["p-columnas"]) - 1
    m = max(representacion["filas"]) + 1
    matriz = [[0] * n for _ in range(m)]
    for columna in range(n):
        inicio = representacion["p-columnas"][columna]
        fin = representacion["p-columnas"][columna + 1]
        for idx in range(inicio, fin):
            matriz[representacion["filas"][idx]][columna] = representacion["valores"][idx]
    return matriz



def cargar_representacion(archivo, formato):
    """
    Carga una representación de matriz desde un archivo.

    Args:
        archivo (str): Ruta del archivo.
        formato (str): Formato de la representación ("COO", "CSR", "CSC").

    Returns:
        dict: Representación de la matriz.
    """
    with open(archivo, 'r') as f:
        contenido = {line.split(":")[0].strip(): line.split(":")[1].strip() for line in f.readlines()}
    
    if formato == "COO":
        return {
            "valores": list(map(int, contenido["valores"].strip("[]").split())),
            "filas": list(map(int, contenido["filas"].strip("[]").split())),
            "columnas": list(map(int, contenido["columnas"].strip("[]").split()))
        }
    elif formato == "CSR":
        return {
            "valores": list(map(int, contenido["valores"].strip("[]").split())),
            "columnas": list(map(int, contenido["columnas"].strip("[]").split())),
            "p-filas": list(map(int, contenido["p-filas"].strip("[]").split()))
        }
    elif formato == "CSC":
        return {
            "valores": list(map(int, contenido["valores"].strip("[]").split())),
            "filas": list(map(int, contenido["filas"].strip("[]").split())),
            "p-columnas": list(map(int, contenido["p-columnas"].strip("[]").split()))
        }
    else:
        raise ValueError("Formato no soportado.")






if __name__ == "__main__":
    menu_principal()
