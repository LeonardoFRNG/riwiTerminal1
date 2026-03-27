#importamos csv 
import csv

def guardar_csv(inventario, ruta="inventario.csv"):
    """
    Guarda el inventario en un archivo CSV.
    Parámetros: inventario (list), ruta (str) - nombre del archivo
    Return: None
    """
    if len(inventario) == 0:
        print("No hay productos en el inventario para guardar.")
        return
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["nombre", "precio", "cantidad"]) #estev es el encabezado
            for producto in inventario:
                writer.writerow([producto["nombre"], producto["precio"], producto["cantidad"]])
        print(f"Inventario guardado en {ruta}")
    except:
        print("Error al guardar el archivo.")
    
def cargar_csv(inventario, ruta="inventario.csv"):
    """
    Carga los productos desdfe un archivo CSV al inventario..
    Parámetros: inventario (list), ruta (str) - nombre del archivo
    Retorno: None
    """

    try:
        #newline es para los salos de linea, para qu no lls haga y encoding utf-8 es para que acepte caracteres especiales y lo haya error en la escritura
        with open(ruta, "r", newline="", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            encabezado = next(reader)  # leemos la primera fila

            # Validamos que el encabezado sea correcto
            if encabezado != ["nombre", "precio", "cantidad"]:
                print("El archivo no tiene el formato correcto.")
                return

            # Leemos las filas y validamos cada una
            productos_validos = []
            filas_invalidas = 0

            for fila in reader:
                try:
                    # Validamos que tenga exactamente 3 columnas
                    if len(fila) != 3:
                        filas_invalidas += 1
                        continue

                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    # Validamos que no sean negativos
                    if precio < 0 or cantidad < 0:
                        filas_invalidas += 1
                        continue

                    productos_validos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

                except:
                    filas_invalidas += 1
                    continue

    except FileNotFoundError:#este except se ejecuta cuando el archivo no existe
        print(f"No se encontró el archivo '{ruta}'.")
        return
    except UnicodeDecodeError:#este se ejecuta cuando el archivo tiene caracteres raros o que no fueron guardados con utf-8
        print("Error al leer el archivo, verifique que sea un CSV válido.")
        return
    except:
        print("Error inesperado al cargar el archivo.")
        return

    
    print(f"\nSe encontraron {len(productos_validos)} productos válidos.")
    opcion = input("¿Sobrescribir inventario actual? (S/N): \n").upper()

    if opcion == "S":
        inventario.clear()  # vaciamos el inventario actual
        #la funcion .extend es para agregar los elmentos de una lista a otra 
        inventario.extend(productos_validos)  # agregamos los nuevos
        print("Inventario reemplazado correctamente.")
    else:
        #aca se fusionan los nomnbres
        print("Política de fusión: si el producto ya existe, se suma la cantidad y se actualiza el precio.")
        for p in productos_validos:
            existe = False
            for actual in inventario:
                if actual["nombre"].lower() == p["nombre"].lower():
                    actual["cantidad"] += p["cantidad"]  # sumamos cantidad
                    actual["precio"] = p["precio"]       # actualizamos precio
                    existe = True
                    break
            if not existe:
                inventario.append(p)  # si no existe lo agregamos
        print("Inventario fusionado correctamente.")

    
    print(f"\nRESUMEN DE CARGA:")
    print(f"  Productos cargados:  {len(productos_validos)}")
    print(f"  Filas inválidas:     {filas_invalidas}")
    print(f"  Acción:              {'Reemplazo' if opcion == 'S' else 'Fusión'}")