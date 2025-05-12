# Vamos a empezar creando una lista para guardar la información de nuestros libros.
# Cada libro será un "diccionario", que es como una pequeña caja donde guardamos información con etiquetas (claves) y su valor.
inventario = []

# Ahora, vamos a crear algunos libros iniciales para que nuestro inventario no esté vacío.
# Usaremos la misma estructura de diccionario con las claves 'titulo', 'precio' y 'cantidad'.
libro1:dict = {"titulo": "El Principito", "precio": 15.50, "cantidad": 10} # segun recomendacion TL: asignar el tipo de dato para todas las variables: (int,str,dict,float,list,tuple)
libro2:dict = {"titulo": "Cien años de soledad", "precio": 22.00, "cantidad": 5}
libro3:dict = {"titulo": "Don Quijote de la Mancha", "precio": 30.75, "cantidad": 3}
libro4:dict = {"titulo": "Orgullo y prejuicio", "precio": 18.90, "cantidad": 8}
libro5:dict = {"titulo": "Harry Potter y la piedra filosofal", "precio": 25.20, "cantidad": 12}

# Agregamos estos libros iniciales a nuestra lista de inventario.
inventario.append(libro1)
inventario.append(libro2)
inventario.append(libro3)
inventario.append(libro4)
inventario.append(libro5)

# ¡Ya tenemos nuestro inventario inicial con 5 libros!

# --------------------------------------------------------------------------
# 1. Función para añadir un nuevo libro al inventario
# --------------------------------------------------------------------------
def agregar_libro() -> None: # Si la funcion no retorna nada, se pone none como tipo de dato 
    print("\n--- Añadir Nuevo Libro ---")
    # Pedimos al usuario que ingrese la información del nuevo libro.
    nuevo_titulo = input("Ingresa el título del libro: ")
    # Vamos a asegurarnos de que el precio sea un número positivo.
    while True:
        try:
            nuevo_precio_str = input("Ingresa el precio del libro: ")
            nuevo_precio = float(nuevo_precio_str)
            if nuevo_precio > 0:
                break
            else:
                print("El precio debe ser un número positivo.")
        except ValueError:
            print("Por favor, ingresa un número válido para el precio.")

    # También nos aseguramos de que la cantidad sea un número entero positivo.
    while True:
        try:
            nueva_cantidad_str = input("Ingresa la cantidad disponible: ")
            nueva_cantidad = int(nueva_cantidad_str)
            if nueva_cantidad >= 0:
                break
            else:
                print("La cantidad debe ser un número positivo o cero.")
        except ValueError:
            print("Por favor, ingresa un número entero válido para la cantidad.")

    # Creamos un nuevo diccionario con la información del libro.
    nuevo_libro = {"titulo": nuevo_titulo, "precio": nuevo_precio, "cantidad": nueva_cantidad}
    # Añadimos este nuevo diccionario a nuestra lista de inventario.
    inventario.append(nuevo_libro)
    print(f"El libro '{nuevo_titulo}' ha sido añadido al inventario.")

# --------------------------------------------------------------------------
# 2. Función para consultar un libro en el inventario por su título
# --------------------------------------------------------------------------
def consultar_libro():
    print("\n--- Consultar Libro ---")
    titulo_buscar = input("Ingresa el título del libro que deseas buscar: ")
    encontrado = False
    # Recorremos cada libro en nuestra lista de inventario.
    for libro in inventario:
        # Comparamos el título que ingresó el usuario con el título del libro actual.
        if libro["titulo"].lower() == titulo_buscar.lower():
            # Si los títulos coinciden (ignorando si son mayúsculas o minúsculas), mostramos la información del libro.
            print(f"Título: {libro['titulo']}")
            print(f"Precio: ${libro['precio']:.2f}") # El :.2f es para mostrar el precio con dos decimales.
            print(f"Cantidad disponible: {libro['cantidad']}")
            encontrado = True
            break # Si encontramos el libro, no necesitamos seguir buscando.
    # Si después de revisar todos los libros no encontramos el título, mostramos un mensaje.
    if not encontrado:
        print(f"El libro '{titulo_buscar}' no se encuentra en el inventario.")

# --------------------------------------------------------------------------
# 3. Función para actualizar el precio de un libro
# --------------------------------------------------------------------------
def actualizar_precio():
    print("\n--- Actualizar Precio de Libro ---")
    titulo_actualizar = input("Ingresa el título del libro cuyo precio deseas actualizar: ")
    encontrado = False
    # Buscamos el libro por su título.
    for libro in inventario:
        if libro["titulo"].lower() == titulo_actualizar.lower():
            encontrado = True
            # Si encontramos el libro, pedimos el nuevo precio.
            while True:
                try:
                    nuevo_precio_str = input("Ingresa el nuevo precio del libro: ")
                    nuevo_precio = float(nuevo_precio_str)
                    if nuevo_precio > 0:
                        # Actualizamos el precio del libro.
                        libro["precio"] = nuevo_precio
                        print(f"El precio de '{libro['titulo']}' ha sido actualizado a ${nuevo_precio:.2f}.")
                        break # Salimos del bucle de validación del precio.
                    else:
                        print("El precio debe ser un número positivo.")
                except ValueError:
                    print("Por favor, ingresa un número válido para el precio.")
            break # Salimos del bucle de búsqueda del libro.
    # Si no encontramos el libro, mostramos un mensaje.
    if not encontrado:
        print(f"El libro '{titulo_actualizar}' no se encuentra en el inventario.")

# --------------------------------------------------------------------------
# 4. Función para eliminar un libro del inventario
# --------------------------------------------------------------------------
def eliminar_libro():
    print("\n--- Eliminar Libro del Inventario ---")
    titulo_eliminar = input("Ingresa el título del libro que deseas eliminar: ")
    encontrado_indice = -1 # Usaremos esto para recordar la posición del libro si lo encontramos.
    # Recorremos la lista de inventario con su índice.
    for indice, libro in enumerate(inventario):
        if libro["titulo"].lower() == titulo_eliminar.lower():
            encontrado_indice = indice
            break # Encontramos el libro, no necesitamos seguir buscando.

    # Si encontramos el libro, pedimos confirmación antes de eliminarlo.
    if encontrado_indice != -1:
        confirmacion = input(f"¿Estás seguro de que deseas eliminar '{inventario[encontrado_indice]['titulo']}'? (s/n): ")
        if confirmacion.lower() == 's':
            # Eliminamos el libro de la lista usando el índice que guardamos.
            libro_eliminado = inventario.pop(encontrado_indice)
            print(f"El libro '{libro_eliminado['titulo']}' ha sido eliminado del inventario.")
        else:
            print("No se ha eliminado el libro.")
    else:
        print(f"El libro '{titulo_eliminar}' no se encuentra en el inventario.")

# --------------------------------------------------------------------------
# 5. Función para calcular el valor total del inventario
# --------------------------------------------------------------------------
def calcular_valor_total():
    valor_total = 0
    # Recorremos cada libro en el inventario.
    for libro in inventario:
        # Multiplicamos el precio del libro por su cantidad y sumamos al valor total.
        valor_total += libro["precio"] * libro["cantidad"]
    # Mostramos el valor total con dos decimales.
    print(f"\nEl valor total del inventario es: ${valor_total:.2f}")

# --------------------------------------------------------------------------
# Menú principal del programa
# --------------------------------------------------------------------------
while True:
    print("\n--- Gestión de Inventario de Librería ---")
    print("Selecciona una opción:")
    print("1. Añadir libro al inventario")
    print("2. Consultar libro en inventario")
    print("3. Actualizar precio de libro")
    print("4. Eliminar libro del inventario")
    print("5. Calcular el valor total del inventario")
    print("6. Salir")

    opcion = input("Ingresa el número de la opción deseada: ")
def main():
    if opcion == '1':
        agregar_libro()
    elif opcion == '2':
        consultar_libro()
    elif opcion == '3':
        actualizar_precio()
    elif opcion == '4':
        eliminar_libro()
    elif opcion == '5':
        calcular_valor_total()
    elif opcion == '6':
        print("¡Gracias por usar el sistema de gestión de inventario!")
        break # Salimos del bucle principal y el programa termina.
    else:
        print("Opción inválida. Por favor, intenta de nuevo.")

main()
