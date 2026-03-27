
#importamos todas las funciones desde servicios
from servicios import (agregar_producto, mostrar_inventario, buscar_producto,
                        actualizar_producto, eliminar_producto, calcular_estadisticas)
from archivos import guardar_csv, cargar_csv

# Lista principal del inventario
inventario = []

while True:
    print("\n===== MENU INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    opcion = input("Ingrese una opción (1-9): \n")

    if opcion == "1":
        agregar_producto(inventario)
    elif opcion == "2":
        mostrar_inventario(inventario)
    elif opcion == "3":
        buscar_producto(inventario)
    elif opcion == "4":
        actualizar_producto(inventario)
    elif opcion == "5":
        eliminar_producto(inventario)
    elif opcion == "6":
        calcular_estadisticas(inventario)
    elif opcion == "7":
        guardar_csv(inventario)
    elif opcion == "8":
        cargar_csv(inventario)
    elif opcion == "9":
        print(" Saliste, vuelve pronto!")
        break
    else:
        print(" Opción inválida, intente de nuevo.")
        