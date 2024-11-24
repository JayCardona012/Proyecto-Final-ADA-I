def obtener_elemento(representacion, formato, i, j):
    """
    Obtiene un elemento de la matriz dispersa dado su índice (i, j).

    Args:
        representacion (dict): La representación de la matriz dispersa.
        formato (str): El formato de la matriz ("COO", "CSR", "CSC").
        i (int): Índice de la fila.
        j (int): Índice de la columna.

    Returns:
        int/float: El valor del elemento en la posición (i, j).
    """
    if formato == "COO":
        filas = representacion["filas"]
        columnas = representacion["columnas"]
        valores = representacion["valores"]
        for idx, (fila, columna) in enumerate(zip(filas, columnas)):
            if fila == i and columna == j:
                return valores[idx]
        return 0  # Elemento no está en la representación, es un cero.

    elif formato == "CSR":
        valores = representacion["valores"]
        columnas = representacion["columnas"]
        p_filas = representacion["p-filas"]

        if i < 0 or i >= len(p_filas) - 1:
            raise IndexError("Índice de fila fuera de rango.")
        inicio = p_filas[i]
        fin = p_filas[i + 1]
        for idx in range(inicio, fin):
            if columnas[idx] == j:
                return valores[idx]
        return 0

    elif formato == "CSC":
        valores = representacion["valores"]
        filas = representacion["filas"]
        p_columnas = representacion["p-columnas"]

        if j < 0 or j >= len(p_columnas) - 1:
            raise IndexError("Índice de columna fuera de rango.")
        inicio = p_columnas[j]
        fin = p_columnas[j + 1]
        for idx in range(inicio, fin):
            if filas[idx] == i:
                return valores[idx]
        return 0

    else:
        raise ValueError("Formato de representación no válido.")


def seleccionar_formato():
    """
    Muestra un menú para seleccionar el formato de la representación.

    Returns:
        str: El formato seleccionado ("COO", "CSR", "CSC").
    """
    while True:
        print("\n--- Selección de Formato ---")
        print("1. Formato COO")
        print("2. Formato CSR")
        print("3. Formato CSC")
        opcion = input("Seleccione un formato: ")
        
        if opcion == "1":
            return "COO"
        elif opcion == "2":
            return "CSR"
        elif opcion == "3":
            return "CSC"
        else:
            print("Opción inválida. Intente nuevamente.")