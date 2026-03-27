#servicios.py

def agregar_producto (inventario):
    """
    Pide nombre, precio y cantidad al usuario y agrega el producto al inventario.
    Parámetros: inventario 
    Retorno: None
    """
    #pedir nombre(no necesita validacion)
    while True:
        nombre = input("Ingrese el nombre del producto: \n")
        if nombre.replace(" ", "").isalpha(): #.replace cambia los espacios por nada osea como que los elimina. y .isalpha() revisa que solo sean letras lo que se ingrese, los dos jutnos: primero elimina espacios, luego verifica que todo sea letras. 
            break
        else:
            print("Solo puedes ingresar letras, intente de nuevo.")
    # pedir precio (si necesita validacion)
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: \n"))
            if precio < 0:
                print("El precio debe ser positivo, intente de nuevo.")
            else:
                break #hasta que se ingrese algo valido o correcto
        except:
            print("Valor invalido, intente nuevamente.") #si el usuario ingresa un valor invalido salta el mensaje del print y se ejecuta el except
    # pedir cantidad (necesita validacion)        
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: \n"))
            if cantidad < 0:
                print("La cantidad debe ser positiva, intente de nuevo.")
            else:
                break
        except:
            print("Cantidad invalda, intente nuevamente.")
            
    # crear diccionario y guardar        
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print(f"Producto: {nombre} agregado correctamente! ")
    
def mostrar_inventario (inventario):
    """
    Muestra todos los productos del inventario.
    Parámetros: inventario
    Retorno: None
    """
    if len(inventario) == 0:#recorremos toda la lista y se verifica si esta o no vacia
        print("El inventario esta vacio. ")
    else:
        print("\n Inventario actual: ")
        print("-" * 45)
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']:.2f} | Cantidad: {producto['cantidad']}")#el :.2f es solamente que le dice a py que ponga dos decimales 2.00, 5.98
        print("-" * 45)
    
def buscar_producto (inventario):
    """
    Pide un nombre al usuario y busca el producto en el inventario.
    Parámetros: inventario 
    Retorno: el diccionario del producto si lo encuentra, None si no existe
    """
    nombre = input("Ingrese el nombre del producto a bscar: \n")
    
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower(): #si producto es iggual a nombre entonces imprime producto encontrado, .lower solo cambia los caracteres a minusculas para compararlos.
            print("\n Producto encontrado: ")
            print(f"Nombre: {producto['nombre']} | Precio: {producto['precio']:.2f} | Cantidad: {producto['cantidad']}")
            return producto
        else:
            print(f"Producto: {nombre} no encontradop. ")
            return None

def actualizar_producto (inventario):
    """
    Pide un nombre al usuario y permite actualizar su precio o cantidad.
    Parámetros: inventario 
    Retorno: None
    """
    nombre = input("Ingrese el nombre del producto a actualizar: \n")
    
    #buscamos el producto
    producto = None
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            producto = p
            break
        
    if producto is None:
        print(f"Producto: {nombre} no encontrado.")
        return
    
    #aqctualizamos precio
    while True:
        try:
            nuevo_precio = float(input(f"Ingrese el nuevo precio (actual: {producto['precio']:.2f}): \n"))
            if nuevo_precio < 0:
                print("El precio debe ser positivo, intente de nuevo. ")
            else:
                producto["precio"] = nuevo_precio
                break
        except:
            print("Valor invalido, ingrese nuevamente.")
    
    #actualizAR CAntidad
    while True:
        try:
            nueva_cantidad = int(input(f"Ingrese la nueva cantidad (actual: {producto['cantidad']}): \n")) 
            if nueva_cantidad < 0:
                print("La nueva cantidad debe ser positiva, intente de nuevo. ")
            else:
                producto["cantidad"] = nueva_cantidad
                break
        except:
            print("Cantidad invalida, ingrese nu8evamente. ")
    
    print(f"Producto: {nombre} actualizado correctamente. ")
    
def eliminar_producto (inventario):
    """
    Pide un nombre al usuario y elimina el producto del inventario.
    Parámetros: inventario 
    Retorno: None
    """
    nombre = input("Ingrese el nombre del producto a eliminar: \n")
    
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            inventario.remove(producto)
            print(f"Producto: {nombre} eliminado correctamente. ")
            return
    print(f"Producto: {nombre} no encontrado.")
    
def calcular_estadisticas (inventario):
    """
    Calcula y muestra estadísticas del inventario.
    Parámetros: inventario 
    Retorno: None
    """
    if len(inventario) == 0:
        print("No hay ningun producto en el inventario. ")
        return
    
    #lambda paraq calcular el subtotal de cada producto
    subtotal = lambda p: p["precio"] * p["cantidad"]
    
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mas_barato = min(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    print("\n ESTADÍSTICAS DEL INVENTARIO:")
    print("-" * 45)
    print(f"  Unidades totales:     {unidades_totales}")
    print(f"  Valor total:          ${valor_total:.2f}")
    print(f"  Producto más caro:    {producto_mas_caro['nombre']} (${producto_mas_caro['precio']:.2f})")
    print(f"  Producto más barato:  {producto_mas_barato['nombre']} (${producto_mas_barato['precio']:.2f})")
    print(f"  Mayor stock:          {producto_mayor_stock['nombre']} ({producto_mayor_stock['cantidad']} unidades)")
    print("-" * 45)