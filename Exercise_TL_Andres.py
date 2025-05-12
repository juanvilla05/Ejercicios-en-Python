from typing import List, Dict, Optional

# Nuestra "base de datos" de libros. Será una lista donde cada libro es un diccionario.
biblioteca: List[Dict[str, any]] = []

# Lista de géneros literarios permitidos.
generos_validos: List[str] = ["Fiction", "Non-Fiction", "Science", "Biography", "Children"]

def agregar_libro() -> None:
    """Permite añadir un nuevo libro a la biblioteca."""
    print("\n--- Añadir Nuevo Libro ---")
    titulo: str = input("Título del libro: ")
    autor: str = input("Autor del libro: ")
    # Vamos a asegurarnos de que la cantidad sea un número entero.
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

    # Validamos el género contra nuestra lista de géneros permitidos.
    while True:
        genero: str = input(f"Género literario ({', '.join(generos_validos)}): ").capitalize()
        if genero in generos_validos:
            break
        else:
            print(f"Género no válido. Por favor, elige entre: {', '.join(generos_validos)}.")

    # Creamos un diccionario que representa el libro.
    nuevo_libro: Dict[str, any] = {
        "titulo": titulo,
        "autor": autor,
        "cantidad": cantidad,
        "genero": genero,
        "total_copias": cantidad # Guardamos la cantidad original para la eliminación.
    }
    biblioteca.append(nuevo_libro)
    print(f"\n¡El libro '{titulo}' ha sido añadido a la biblioteca!")

def buscar_libro() -> None:
    """Permite buscar los detalles de un libro por su título."""
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
    """Registra el préstamo de un libro, disminuyendo la cantidad disponible."""
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
    """Registra la devolución de un libro, aumentando la cantidad disponible."""
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
    """Permite eliminar un libro del catálogo si no tiene copias prestadas."""
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
    """Muestra todos los libros disponibles de un género específico."""
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
    """Indica cuántos libros y copias totales hay en la biblioteca."""
    print("\n--- Resumen del Inventario ---")
    total_libros: int = len(biblioteca)
    total_copias_disponibles: int = sum(libro["cantidad"] for libro in biblioteca)
    print(f"Total de libros en la biblioteca: {total_libros}")
    print(f"Total de copias disponibles: {total_copias_disponibles}")

def main() -> None:
    """Función principal que ejecuta el sistema de gestión de biblioteca."""
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

        opcion: str = input("Elige una opción (1-8): ")

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
            print("\n¡Gracias por usar el sistema de gestión de biblioteca!")
            break
        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 8.")

# --- Inicialización con al menos 10 libros para probar ---
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
    {"titulo": "Fundación", "autor": "Isaac Asimov", "cantidad": 3, "genero": "Science", "total_copias": 3} # Un libro extra para tener más de 10.
]

for libro_inicial in agregar_libro_inicial:
    biblioteca.append(libro_inicial)

print("\n¡Se han añadido 11 libros iniciales para probar el sistema!")

if __name__ == "__main__":
    main()
