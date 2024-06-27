GENEROS = ["accion","ficcion","terror"]

def registrar_libros(libros):
    titulo_libro = input("Ingrese el título del libro: ").lower()
    while titulo_libro == "":
        print("Debe ingresar un título")
        titulo_libro = input("Ingrese el título del libro: ").lower()
    autor = input("Ingrese el autor del libro: ").lower()
    while autor == "":
        print("Debe ingresar el autor")
        autor = input("Ingrese el autor del libro: ").lower()
    genero = input("ingrese el género del libro: ").lower()
    while genero == "":
        print("Debe ingresar un género")
        genero = input("ingrese el género del libro: ").lower()
    precio = int(input("Ingrese el precio del libro: "))
    while genero == "":
        print("Debe ingresar el precio")
        precio = int(input("Ingrese el precio del libro: "))
    libros.append({
        'Titulo':titulo_libro,
        'Autor':autor,
        'Genero':genero,
        'Precio':precio
    })
    print(f"\n{libros}\n")

def listar_todos_los_libros(libros):
    print("\n                      Lista de libros   \n")
    for libro in libros:
        print(libro)

def registrar_venta(libros):
    titulo_libro = input("Ingrese el título del libro: ").lower()
    cantidad = int(input("Ingrese la cantidad de este libro que desea: "))
    precio = int(input("Ingrese el precio del libro"))


def imprimir_reporte_de_ventas(libros):
    genero_seleccionado = input("Si necesitas impimir un género en específico, escribelo, si quieres imprimirlos todos presiona ENTER")
    if genero_seleccionado == "":
        imprimir_todos = libros
        nombre_archivo = "planilla_todos.txt"
    elif genero_seleccionado in GENEROS:
        imprimir_todos = []
        for libro in libros:
            if libro ['Genero'] in GENEROS:
                imprimir_todos.append(libro)
        nombre_archivo = (f"planilla_{genero_seleccionado}.txt")
    with open(nombre_archivo, "w") as archivo:
        for libro in imprimir_todos:
            archivo.write(f"Titulo:{libro['Titulo']}\n")
            archivo.write(f"Autor:{libro['Autor']}\n")
            archivo.write(f"Género:{libro['Genero']}\n")
            archivo.write(f"Titulo:{libro['Titulo']}\n")