import funciones as fn
libros = []
while True:
    try:
        print("\n        **LIBRERÍA BOSS**\n\n(1) Registrar libros\n(2) Listar todos los libros\n(3) Registrar venta\n(4) Imprimir reporte de ventas\n(5) Salir del programa")
        opcion = int(input("¿Que desea hacer? "))
        if opcion ==1:
            fn.registrar_libros(libros)
        elif opcion ==2:
              fn.listar_todos_los_libros(libros)
        elif opcion ==3:
              fn.registrar_venta(libros)
        elif opcion ==4:
              fn.imprimir_reporte_de_ventas(libros)
        elif opcion ==5:
              print("Adiós!")
              break
        else:
              print("\nOpción inválida, vuelv a ingresar un opción\n")                        
    except ValueError:
         print("\nEsto es inválido\n")