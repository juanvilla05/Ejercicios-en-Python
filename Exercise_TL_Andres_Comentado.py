# --- Inicialización ---

# 'biblioteca' es una lista vacía que actuará como nuestra base de datos de libros.
# Cada libro dentro de esta lista será representado por un diccionario.
biblioteca = []

# 'generos_validos' es una lista que contiene los géneros de libros que aceptaremos en nuestro sistema.
# Esto nos ayuda a mantener la información organizada y evitar errores de escritura.
generos_validos = ["Fiction", "Non-Fiction", "Science", "Biography", "Children"]

# --- Funciones del Sistema ---

def agregar_libro():
    """
    Esta función permite al usuario añadir un nuevo libro a la biblioteca.
    Le pide la información necesaria (título, autor, cantidad, género) y
    guarda esa información como un nuevo diccionario dentro de la lista 'biblioteca'.
    """
    print("\n--- Añadir Nuevo Libro ---")
    # Pedimos al usuario que ingrese el título del libro y lo guardamos en la variable 'titulo'.
    titulo = input("Título del libro: ")
    # Pedimos el nombre del autor y lo guardamos en 'autor'.
    autor = input("Autor del libro: ")
    # Iniciamos un bucle 'while True' para asegurarnos de que el usuario ingrese una cantidad válida (un número entero positivo).
    while True:
        try:
            # Intentamos convertir la entrada del usuario a un número entero usando 'int()'.
            cantidad = int(input("Cantidad de copias disponibles: "))
            # Si la cantidad es mayor o igual a 0, es válida y salimos del bucle con 'break'.
            if cantidad >= 0:
                break
            # Si la cantidad es negativa, mostramos un mensaje de error.
            else:
                print("La cantidad debe ser un número positivo.")
        # Si el usuario ingresa algo que no se puede convertir a un número entero, ocurre un 'ValueError'.
        # El bloque 'except' captura este error y muestra un mensaje amigable.
        except ValueError:
            print("Por favor, escribe un número entero para la cantidad.")

    # Iniciamos otro bucle 'while True' para asegurarnos de que el usuario elija un género de la lista 'generos_validos'.
    while True:
        # Pedimos al usuario que ingrese el género y usamos '.capitalize()' para poner la primera letra en mayúscula
        # para que coincida con la forma en que están guardados los géneros en nuestra lista.
        genero = input(f"Género literario ({', '.join(generos_validos)}): ").capitalize()
        # Si el género ingresado está en nuestra lista de géneros válidos, salimos del bucle.
        if genero in generos_validos:
            break
        # Si el género no es válido, mostramos un mensaje de error y la lista de géneros permitidos.
        else:
            print(f"Género no válido. Por favor, elige entre: {', '.join(generos_validos)}.")

    # Creamos un diccionario llamado 'nuevo_libro' para almacenar la información del libro.
    # Las claves (como "titulo", "autor") nos permiten acceder a los valores correspondientes.
    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "cantidad": cantidad,
        "genero": genero,
        "total_copias": cantidad # Guardamos la cantidad original de copias para la función de eliminar.
    }
    # Añadimos este nuevo diccionario a nuestra lista 'biblioteca' usando el método '.append()'.
    biblioteca.append(nuevo_libro)
    # Mostramos un mensaje de confirmación al usuario.
    print(f"\n¡El libro '{titulo}' ha sido añadido a la biblioteca!")

def buscar_libro():
    """
    Esta función permite al usuario buscar un libro por su título.
    Recorre la lista 'biblioteca' y si encuentra un libro con el título buscado,
    muestra sus detalles (autor, copias disponibles, género).
    """
    print("\n--- Buscar Libro ---")
    # Pedimos al usuario que ingrese el título del libro que está buscando.
    titulo_buscar = input("Escribe el título del libro que buscas: ")
    # Usamos una variable booleana 'encontrado' para saber si encontramos el libro o no. Inicialmente es False.
    encontrado = False
    # Recorremos cada 'libro' (que es un diccionario) en nuestra lista 'biblioteca'.
    for libro in biblioteca:
        # Comparamos el título del libro actual (convertido a minúsculas con '.lower()')
        # con el título que el usuario ingresó (también convertido a minúsculas).
        # Esto hace que la búsqueda no distinga entre mayúsculas y minúsculas.
        if libro["titulo"].lower() == titulo_buscar.lower():
            print("\nDetalles del libro:")
            print(f"  Título: {libro['titulo']}")
            print(f"  Autor: {libro['autor']}")
            print(f"  Copias disponibles: {libro['cantidad']}")
            print(f"  Género: {libro['genero']}")
            # Si encontramos el libro, cambiamos 'encontrado' a True.
            encontrado = True
            # 'break' se utiliza para salir del bucle 'for' una vez que encontramos el libro,
            # ya que no necesitamos seguir buscando.
            break
    # Si después de revisar todos los libros, 'encontrado' sigue siendo False, significa que no se encontró el libro.
    if not encontrado:
        print(f"\nLo siento, el libro '{titulo_buscar}' no se encuentra en la biblioteca.")

def prestar_libro():
    """
    Esta función permite registrar el préstamo de un libro.
    Busca el libro por título y si hay copias disponibles (cantidad > 0),
    disminuye la cantidad en 1.
    """
    print("\n--- Prestar Libro ---")
    # Pedimos al usuario el título del libro que quiere prestar.
    titulo_prestar = input("Escribe el título del libro que quieres prestar: ")
    # Variable para verificar si el libro fue encontrado.
    encontrado = False
    # Recorremos la lista de libros.
    for libro in biblioteca:
        # Si encontramos el libro...
        if libro["titulo"].lower() == titulo_prestar.lower():
            # Verificamos si hay copias disponibles.
            if libro["cantidad"] > 0:
                # Si hay copias, restamos 1 a la cantidad disponible.
                libro["cantidad"] -= 1
                print(f"\n¡El libro '{libro['titulo']}' ha sido prestado!")
                print(f"Ahora quedan {libro['cantidad']} copias disponibles.")
            # Si no hay copias disponibles, mostramos un mensaje.
            else:
                print(f"\nLo siento, no hay copias disponibles del libro '{libro['titulo']}'.")
            # Marcamos que encontramos el libro y salimos del bucle.
            encontrado = True
            break
    # Si no se encontró el libro, mostramos un mensaje.
    if not encontrado:
        print(f"\nLo siento, el libro '{titulo_prestar}' no se encuentra en la biblioteca.")

def devolver_libro():
    """
    Esta función registra la devolución de un libro.
    Busca el libro por título y aumenta en 1 la cantidad de copias disponibles.
    """
    print("\n--- Devolver Libro ---")
    # Pedimos el título del libro que se está devolviendo.
    titulo_devolver = input("Escribe el título del libro que estás devolviendo: ")
    # Variable para verificar si el libro fue encontrado.
    encontrado = False
    # Recorremos la lista de libros.
    for libro in biblioteca:
        # Si encontramos el libro...
        if libro["titulo"].lower() == titulo_devolver.lower():
            # Aumentamos en 1 la cantidad de copias disponibles.
            libro["cantidad"] += 1
            print(f"\n¡El libro '{libro['titulo']}' ha sido devuelto!")
            print(f"Ahora hay {libro['cantidad']} copias disponibles.")
            # Marcamos que lo encontramos y salimos del bucle.
            encontrado = True
            break
    # Si no se encontró el libro, mostramos un mensaje.
    if not encontrado:
        print(f"\nLo siento, el libro '{titulo_devolver}' no se encuentra en la biblioteca.")

def eliminar_libro():
    """
    Esta función permite eliminar un libro del catálogo.
    Solo se puede eliminar si no hay copias prestadas (cantidad disponible
    es igual a la cantidad total original).
    """
    print("\n--- Eliminar Libro ---")
    # Pedimos el título del libro que se quiere eliminar.
    titulo_eliminar = input("Escribe el título del libro que quieres eliminar: ")
    # Variable para guardar el índice del libro a eliminar. Inicialmente -1 (no encontrado).
    indice_eliminar = -1
    # Recorremos la lista de libros usando 'enumerate' para obtener el índice y el libro.
    for i, libro in enumerate(biblioteca):
        # Si encontramos el libro...
        if libro["titulo"].lower() == titulo_eliminar.lower():
            # Verificamos si la cantidad disponible es igual a la cantidad total original.
            if libro["cantidad"] == libro["total_copias"]:
                # Si es así, guardamos el índice del libro.
                indice_eliminar = i
                # Salimos del bucle ya que encontramos el libro a eliminar.
                break
            # Si todavía hay copias prestadas, mostramos un mensaje y salimos del bucle.
            else:
                print(f"\nNo se puede eliminar '{libro['titulo']}'. Todavía hay copias prestadas.")
                break
    # Si encontramos un índice válido para eliminar...
    if indice_eliminar != -1:
        # 'biblioteca.pop(indice_eliminar)' elimina el elemento en ese índice y lo devuelve.
        libro_eliminado = biblioteca.pop(indice_eliminar)
        print(f"\n¡El libro '{libro_eliminado['titulo']}' ha sido eliminado del catálogo!")
    # Si no se encontró el libro para eliminar.
    elif indice_eliminar == -1 and not any(libro["titulo"].lower() == titulo_eliminar.lower() for libro in biblioteca):
        print(f"\nLo siento, el libro '{titulo_eliminar}' no se encuentra en la biblioteca.")

def listar_libros_por_genero():
    """
    Esta función muestra todos los libros disponibles de un género específico
    que el usuario ingrese.
    """
    print("\n--- Listar Libros por Género ---")
    # Pedimos al usuario el género que quiere listar.
    genero_buscar = input(f"Escribe el género que quieres listar ({', '.join(generos_validos)}): ").capitalize()
    # Verificamos si el género ingresado es válido.
    if genero_buscar not in generos_validos:
        print(f"\nGénero no válido. Por favor, elige entre: {', '.join(generos_validos)}.")
        return # Salimos de la función si el género no es válido.

    # Creamos una lista vacía para guardar los títulos de los libros encontrados.
    libros_encontrados = []
    # Recorremos la lista de libros.
    for libro in biblioteca:
        # Si el género del libro coincide con el género buscado...
        if libro["genero"] == genero_buscar:
            # Añadimos el título del libro a la lista de encontrados.
            libros_encontrados.append(libro["titulo"])

    # Mostramos los libros encontrados o un mensaje si no hay ninguno.
    if libros_encontrados:
        print(f"\nLibros de género '{genero_buscar}':")
        for titulo in libros_encontrados:
            print(f"- {titulo}")
    else:
        print(f"\nNo hay libros disponibles del género '{genero_buscar}'.")

def mostrar_resumen_inventario():
    """
    Esta función calcula y muestra la cantidad total de libros únicos
    y la cantidad total de copias disponibles en la biblioteca.
    """
    print("\n--- Resumen del Inventario ---")
    # El número total de libros únicos es simplemente la cantidad de elementos en nuestra lista 'biblioteca'.
    total_libros = len(biblioteca)
    # Calculamos el total de copias disponibles sumando la 'cantidad' de cada libro en la biblioteca.
    total_copias_disponibles = sum(libro["cantidad"] for libro in biblioteca)
    # Mostramos el resumen de forma clara.
    print(f"Total de libros en la biblioteca: {total_libros}")
    print(f"Total de copias disponibles: {total_copias_disponibles}")

# --- Menú Principal ---

# Este bucle 'while True' se ejecuta continuamente hasta que el usuario elige salir.
while True:
    print("\n--- Sistema de Gestión de Biblioteca ---")
    print("1. Añadir libro")
    print("2. Buscar libro por título")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Eliminar libro")
    print("6. Listar libros por género")
    print("7. Mostrar resumen de inventario")
    print("8. Salir")

    # Pedimos al usuario que ingrese su elección del menú.
    opcion = input("Elige una opción (1-8): ")

    # Usamos condicionales 'if', 'elif' (else if), y 'else' para ejecutar la función correspondiente
    # a la opción elegida por el usuario.
    if opcion == '1':
        agregar_libro()
    elif opcion == '2':
        buscar_libro()
    elif opcion == '3':
        prestar_libro()
    elif opcion == '4':
        devolver_libro()
    elif opcion == '5':
        eliminar_libro()
    elif opcion == '6':
        listar_libros_por_genero()
    elif opcion == '7':
        mostrar_resumen_inventario()
    elif opcion == '8':
        # Si el usuario elige '8', mostramos un mensaje de despedida y usamos 'break' para salir del bucle 'while',
        # lo que termina el programa.
        print("\n¡Gracias por usar el sistema de gestión de biblioteca!")
        break
    else:
        # Si el usuario ingresa una opción no válida, mostramos un mensaje de error.
        print("\nOpción no válida. Por favor, elige un número del 1 al 8.")

# --- Inicialización de la Biblioteca con Libros de Ejemplo ---
# Creamos una lista de diccionarios, donde cada diccionario representa un libro con su información.
# Estos libros se añadirán automáticamente a la biblioteca al inicio para que tengamos algunos datos para probar.
agregar_libro_inicial = [
    {"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "cantidad": 5, "genero": "Children", "total_copias": 5},
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "cantidad": 3, "genero": "Fiction", "total_copias": 3},
    {"titulo": "Cosmos", "autor": "Carl Sagan", "cantidad": 2, "genero": "Science", "total_copias": 2},
    {"titulo": "Steve Jobs", "autor": "Walter Isaacson", "cantidad": 4, "genero": "Biography", "total_copias": 4},
    {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "cantidad": 1, "genero": "Fiction", "total_copias": 1},
    {"titulo": "Breve historia del tiempo", "autor": "Stephen Hawking", "cantidad": 3, "genero": "Science", "total_copias": 3},
    {"titulo": "Becoming", "autor": "Michelle Obama", "cantidad": 2, "genero": "Biography", "total_copias": 2},
    {"titulo": "La oruga muy hambrienta", "autor": "Eric Carle", "cantidad": 6, "genero": "Children", "total_copias": 6},
    {"titulo": "Sapiens: De animales a dioses", "autor": "Yuval Noah Harari", "cantidad": 4, "genero": "Non-Fiction", "total_copias": 4},
    {"titulo": "Orgullo y prejuicio", "autor": "Jane Austen", "cantidad": 2, "genero": "Fiction", "total_copias": 2},
    {"titulo": "Fundación", "autor": "Isaac Asimov", "cantidad": 3, "genero": "Science", "total_copias": 3}
]

# Recorremos la lista de libros iniciales y los añadimos a nuestra 'biblioteca'.
for libro_inicial in agregar_libro_inicial:
    biblioteca.append(libro_inicial)

# Mostramos un mensaje indicando que los libros de ejemplo han sido añadidos.
print("\n¡Se han añadido 11 libros iniciales para probar el sistema!")
