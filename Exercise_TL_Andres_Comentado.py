
# --- Inicialización ---

# 'biblioteca' es una lista vacía que actuará como nuestra base de datos de libros.
# Cada libro dentro de esta lista será representado por un diccionario.
biblioteca: List[Dict[str, any]] = []

# 'generos_validos' es una lista que contiene los géneros de libros que aceptaremos en nuestro sistema.
# Esto nos ayuda a mantener la información organizada y evitar errores de escritura.
generos_validos: List[str] = ["Fiction", "Non-Fiction", "Science", "Biography", "Children"]

# --- Funciones del Sistema ---

def agregar_libro() -> None:
    """
    Esta función permite al usuario añadir un nuevo libro a la biblioteca.
    Le pide la información necesaria (título, autor, cantidad, género) y
    guarda esa información como un nuevo diccionario dentro de la lista 'biblioteca'.
    """
    print("\n--- Añadir Nuevo Libro ---")
    titulo: str = input("Título del libro: ")
    autor: str = input("Autor del libro: ")
    while True:
        try:
            cantidad_str: str = input("Cantidad de copias disponibles: ")
            cantidad: int = int(cantidad_str)
            if cantidad >= 0:
                break
            else:
                print("La cantidad debe ser un número positivo.")
        except ValueError:
            print("Por favor, escribe un número entero para la cantidad.")

    while True:
        genero: str = input(f"Género literario ({', '.join(generos_validos)}): ").capitalize()
        if genero in generos_validos:
            break
        else:
            print(f"Género no válido. Por favor, elige entre: {', '.join(generos_validos)}.")

    nuevo_libro: Dict[str, any] = {
        "titulo": titulo,
        "autor": autor,
        "cantidad": cantidad,
        "genero": genero,
        "total_copias": cantidad
    }
    biblioteca.append(nuevo_libro)
    print(f"\n¡El libro '{titulo}' ha sido añadido a la biblioteca!")

def buscar_libro() -> None:
    """
    Esta función permite al usuario buscar un libro por su título.
    Recorre la lista 'biblioteca' y si encuentra un libro con el título buscado,
    muestra sus detalles (autor, copias disponibles, género).
    """
    print("\n--- Buscar Libro ---")
    titulo_buscar: str = input("Escribe el título del libro que buscas: ")
    encontrado: bool = False
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo_buscar.lower():
            print("\nDetalles del libro:")
            print(f"  Título: {libro['titulo']}")
            print(f"  Autor: {libro['autor']}")
            print(f"  Copias disponibles: {libro['cantidad']}")
            print(f"  Género: {libro['genero']}")
            encontrado = True
            break
    if not encontrado:
        print(f"\nLo siento, el libro '{titulo_buscar}' no se encuentra en la biblioteca.")

def prestar_libro() -> None:
    """
    Esta función permite registrar el préstamo de un libro.
    Busca el libro por título y si hay copias disponibles (cantidad > 0),
    disminuye la cantidad en 1.
    """
    print("\n--- Prestar Libro ---")
    titulo_prestar: str = input("Escribe el título del libro que quieres prestar: ")
    encontrado: bool = False
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo_prestar.lower():
            if libro["cantidad"] > 0:
                libro["cantidad"] -= 1
                print(f"\n¡El libro '{libro['titulo']}' ha sido prestado!")
                print(f"Ahora quedan {libro['cantidad']} copias disponibles.")
            else:
                print(f"\nLo siento, no hay copias disponibles del libro '{libro['titulo']}'.")
            encontrado = True
            break
    if not encontrado:
        print(f"\nLo siento, el libro '{titulo_prestar}' no se encuentra en la biblioteca.")

def devolver_libro() -> None:
    """
    Esta función registra la devolución de un libro.
    Busca el libro por título y aumenta en 1 la cantidad de copias disponibles.
    """
    print("\n--- Devolver Libro ---")
    titulo_devolver: str = input("Escribe el título del libro que estás devolviendo: ")
    encontrado: bool = False
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo_devolver.lower():
            libro["cantidad"] += 1
            print(f"\n¡El libro '{libro['titulo']}' ha sido devuelto!")
            print(f"Ahora hay {libro['cantidad']} copias disponibles.")
            encontrado = True
            break
    if not encontrado:
        print(f"\nLo siento, el libro '{titulo_devolver}' no se encuentra en la biblioteca.")

def eliminar_libro() -> None:
    """
    Esta función permite eliminar un libro del catálogo.
    Solo se puede eliminar si no hay copias prestadas (cantidad disponible
    es igual a la cantidad total original).
    """
    print("\n--- Eliminar Libro ---")
    titulo_eliminar: str = input("Escribe el título del libro que quieres eliminar: ")
    indice_eliminar: int = -1
    for i, libro in enumerate(biblioteca):
        if libro["titulo"].lower() == titulo_eliminar.lower():
            if libro["cantidad"] == libro["total_copias"]:
                indice_eliminar = i
                break
            else:
                print(f"\nNo se puede eliminar '{libro['titulo']}'. Todavía hay copias prestadas.")
                break
    if indice_eliminar != -1:
        libro_eliminado: Dict[str, any] = biblioteca.pop(indice_eliminar)
        print(f"\n¡El libro '{libro_eliminado['titulo']}' ha sido eliminado del catálogo!")
    elif indice_eliminar == -1 and not any(libro["titulo"].lower() == titulo_eliminar.lower() for libro in biblioteca):
        print(f"\nLo siento, el libro '{titulo_eliminar}' no se encuentra en la biblioteca.")

def listar_libros_por_genero() -> None:
    """
    Esta función muestra todos los libros disponibles de un género específico
    que el usuario ingrese.
    """
    print("\n--- Listar Libros por Género ---")
    genero_buscar: str = input(f"Escribe el género que quieres listar ({', '.join(generos_validos)}): ").capitalize()
    if genero_buscar not in generos_validos:
        print(f"\nGénero no válido. Por favor, elige entre: {', '.join(generos_validos)}.")
        return

    libros_encontrados: List[str] = []
    for libro in biblioteca:
        if libro["genero"] == genero_buscar:
            libros_encontrados.append(libro["titulo"])

    if libros_encontrados:
        print(f"\nLibros de género '{genero_buscar}':")
        for titulo in libros_encontrados:
            print(f"- {titulo}")
    else:
        print(f"\nNo hay libros disponibles del género '{genero_buscar}'.")

def mostrar_resumen_inventario() -> None:
    """
    Esta función calcula y muestra la cantidad total de libros únicos
    y la cantidad total de copias disponibles en la biblioteca.
    """
    print("\n--- Resumen del Inventario ---")
    total_libros: int = len(biblioteca)
    total_copias_disponibles: int = sum(libro["cantidad"] for libro in biblioteca)
    print(f"Total de libros en la biblioteca: {total_libros}")
    print(f"Total de copias disponibles: {total_copias_disponibles}")

def inicializar_biblioteca() -> None:
    """
    Esta función se encarga de crear e inicializar la lista 'biblioteca'
    con algunos libros de ejemplo para que el sistema tenga datos al iniciar.
    """
    # Definimos una lista de diccionarios llamada 'agregar_libro_inicial'.
    # Cada diccionario representa un libro con su título, autor, cantidad, género y cantidad total de copias.
    agregar_libro_inicial: List[Dict[str, any]] = [
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

    # Recorremos cada libro de la lista 'agregar_libro_inicial'.
    for libro_inicial in agregar_libro_inicial:
        # Añadimos cada diccionario de libro a nuestra lista principal 'biblioteca'.
        biblioteca.append(libro_inicial)

    # Mostramos un mensaje para informar que los libros de ejemplo han sido cargados.
    print("\n¡Se han añadido 11 libros iniciales para probar el sistema!")

def main() -> None:
    """
    Esta es la función principal que se encarga de la lógica general del programa.
    Aquí se llama a la función para inicializar la biblioteca y luego se ejecuta
    el bucle principal que muestra el menú y permite al usuario interactuar con el sistema.
    """
    # Llamamos a la función 'inicializar_biblioteca()' para cargar los libros de ejemplo al inicio.
    inicializar_biblioteca()
    # Iniciamos un bucle 'while True' que se ejecutará continuamente hasta que el usuario decida salir.
    while True:
        # Mostramos el menú de opciones al usuario.
        print("\n--- Sistema de Gestión de Biblioteca ---")
        print("1. Añadir libro")
        print("2. Buscar libro por título")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Eliminar libro")
        print("6. Listar libros por género")
        print("7. Mostrar resumen de inventario")
        print("8. Salir")

        # Pedimos al usuario que ingrese la opción que desea realizar.
        opcion: str = input("Elige una opción (1-8): ")

        # Usamos condicionales 'if', 'elif' (else if), y 'else' para determinar qué función llamar
        # según la opción que el usuario haya ingresado.
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
            # Si el usuario elige la opción '8', mostramos un mensaje de despedida y usamos 'break'
            # para salir del bucle 'while', lo que termina la ejecución del programa.
            print("\n¡Gracias por usar el sistema de gestión de biblioteca!")
            break
        else:
            # Si el usuario ingresa una opción que no está en el menú (no es un número del 1 al 8),
            # mostramos un mensaje indicando que la opción no es válida.
            print("\nOpción no válida. Por favor, elige un número del 1 al 8.")

# --- Punto de entrada del programa ---
# Esta condición '__name__ == "__main__":' se evalúa a True cuando el script se ejecuta directamente.
# Al ser True, se llama a la función 'main()', que inicia la ejecución de nuestro programa.
if __name__ == "__main__":
    main()
