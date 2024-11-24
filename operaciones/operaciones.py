
def obtener_elemento(representacion, formato, i, j):
 
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


def obtener_fila(representacion, formato, i):

    if formato == "COO":
        valores = representacion['valores']
        filas = representacion['filas']
        columnas = representacion['columnas']
        max_col = max(columnas) + 1 if columnas else 0

        fila = [0] * max_col
        for valor, fila_idx, col_idx in zip(valores, filas, columnas):
            if fila_idx == i:
                fila[col_idx] = valor
        return fila

    elif formato == "CSR":
        valores = representacion['valores']
        columnas = representacion['columnas']
        p_filas = representacion['p-filas']
        
        if i >= len(p_filas) - 1:
            raise IndexError("Índice fuera del rango de filas.")
        
        fila = [0] * (max(columnas) + 1 if columnas else 0)
        for idx in range(p_filas[i], p_filas[i + 1]):
            col_idx = columnas[idx]
            fila[col_idx] = valores[idx]
        return fila

    elif formato == "CSC":
        valores = representacion['valores']
        filas = representacion['filas']
        p_columnas = representacion['p-columnas']

        max_fila = max(filas) + 1 if filas else 0
        fila = [0] * max_fila
        for col_idx in range(len(p_columnas) - 1):
            for idx in range(p_columnas[col_idx], p_columnas[col_idx + 1]):
                fila_idx = filas[idx]
                if fila_idx == i:
                    fila[col_idx] = valores[idx]
        return fila

    else:
        raise ValueError("Formato de representación no válido.")

def obtener_columna(representacion, formato, j):

    if formato == "COO":
        valores = representacion['valores']
        filas = representacion['filas']
        columnas = representacion['columnas']
        max_fila = max(filas) + 1 if filas else 0

        columna = [0] * max_fila
        for valor, fila_idx, col_idx in zip(valores, filas, columnas):
            if col_idx == j:
                columna[fila_idx] = valor
        return columna

    elif formato == "CSR":
        valores = representacion['valores']
        columnas = representacion['columnas']
        p_filas = representacion['p-filas']

        max_fila = len(p_filas) - 1
        columna = [0] * max_fila
        for fila_idx in range(max_fila):
            for idx in range(p_filas[fila_idx], p_filas[fila_idx + 1]):
                col_idx = columnas[idx]
                if col_idx == j:
                    columna[fila_idx] = valores[idx]
        return columna

    elif formato == "CSC":
        valores = representacion['valores']
        filas = representacion['filas']
        p_columnas = representacion['p-columnas']

        if j >= len(p_columnas) - 1:
            raise IndexError("Índice fuera del rango de columnas.")

        max_fila = max(filas) + 1 if filas else 0
        columna = [0] * max_fila
        for idx in range(p_columnas[j], p_columnas[j + 1]):
            fila_idx = filas[idx]
            columna[fila_idx] = valores[idx]
        return columna

    else:
        raise ValueError("Formato de representación no válido.")


def modificar_elemento(representacion, formato, i, j, x):

    if formato == "COO":
        valores = representacion['valores']
        filas = representacion['filas']
        columnas = representacion['columnas']

        for idx, (fila, columna) in enumerate(zip(filas, columnas)):
            if fila == i and columna == j:
                if x == 0:  # Si el nuevo valor es 0, eliminar la entrada
                    valores.pop(idx)
                    filas.pop(idx)
                    columnas.pop(idx)
                else:
                    valores[idx] = x
                return representacion

        # Si no se encuentra la posición y x != 0, agregar el nuevo elemento
        if x != 0:
            valores.append(x)
            filas.append(i)
            columnas.append(j)
        return representacion

    elif formato == "CSR":
        valores = representacion['valores']
        columnas = representacion['columnas']
        p_filas = representacion['p-filas']

        start = p_filas[i]
        end = p_filas[i + 1]

        for idx in range(start, end):
            if columnas[idx] == j:
                if x == 0:  # Si el nuevo valor es 0, eliminar la entrada
                    valores.pop(idx)
                    columnas.pop(idx)
                    for k in range(i + 1, len(p_filas)):
                        p_filas[k] -= 1
                else:
                    valores[idx] = x
                return representacion

        # Si no se encuentra la posición y x != 0, agregar el nuevo elemento
        if x != 0:
            valores.insert(end, x)
            columnas.insert(end, j)
            for k in range(i + 1, len(p_filas)):
                p_filas[k] += 1
        return representacion

    elif formato == "CSC":
        valores = representacion['valores']
        filas = representacion['filas']
        p_columnas = representacion['p-columnas']

        start = p_columnas[j]
        end = p_columnas[j + 1]

        for idx in range(start, end):
            if filas[idx] == i:
                if x == 0:  # Si el nuevo valor es 0, eliminar la entrada
                    valores.pop(idx)
                    filas.pop(idx)
                    for k in range(j + 1, len(p_columnas)):
                        p_columnas[k] -= 1
                else:
                    valores[idx] = x
                return representacion

        # Si no se encuentra la posición y x != 0, agregar el nuevo elemento
        if x != 0:
            valores.insert(end, x)
            filas.insert(end, i)
            for k in range(j + 1, len(p_columnas)):
                p_columnas[k] += 1
        return representacion

    else:
        raise ValueError("Formato de representación no válido.")


def guardar_representacion(representacion, formato, archivo_salida):

    with open(archivo_salida, 'w') as f:
        if formato == "COO":
            f.write(f"valores: [{' '.join(map(str, representacion['valores']))}]\n")
            f.write(f"filas: [{' '.join(map(str, representacion['filas']))}]\n")
            f.write(f"columnas: [{' '.join(map(str, representacion['columnas']))}]\n")
        elif formato == "CSR":
            f.write(f"valores: [{' '.join(map(str, representacion['valores']))}]\n")
            f.write(f"columnas: [{' '.join(map(str, representacion['columnas']))}]\n")
            f.write(f"p-filas: [{' '.join(map(str, representacion['p-filas']))}]\n")
        elif formato == "CSC":
            f.write(f"valores: [{' '.join(map(str, representacion['valores']))}]\n")
            f.write(f"filas: [{' '.join(map(str, representacion['filas']))}]\n")
            f.write(f"p-columnas: [{' '.join(map(str, representacion['p-columnas']))}]\n")

