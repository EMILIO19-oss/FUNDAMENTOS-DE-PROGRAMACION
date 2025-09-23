import json

biblioteca = {

    "978-84-376-0494-7": {
        "título": "Cien años de soledad",
        "autor": ["Gabriel García Márquez"],
        "géneros": ["Realismo mágico", "Novela histórica"]
    },
    "978-84-204-1625-5": {
        "título": "Don Quijote de la Mancha",
        "autor": ["Miguel de Cervantes Saavedra"],
        "géneros": ["Novela de caballería", "Satira"]
    },  
    "978-84-264-0026-0": {
        "título": "El nombre del viento",
        "autor": ["Patrick Rothfuss"],
        "géneros": ["Fantasía épica", "Ficción heroica"]
    },
    "978-84-013-5234-8": {
        "título": "1984",
        "autor": ["George Orwell"],
        "géneros": ["Ciencia ficción política", "Ficción especulativa"]
    }
}

isbn = "978-84-376-0494-7"
info_libro = biblioteca.get(isbn)          
print("\nInformación del libro:", info_libro)

isbn = "978-84-204-1625-5"
info_libro = biblioteca.get(isbn)          
print("\nInformación del libro:", info_libro)

isbn = "978-84-264-0026-0"
info_libro = biblioteca.get(isbn)          
print("\nInformación del libro:", info_libro)

isbn = "978-84-013-5234-8"
info_libro = biblioteca.get(isbn)          
print("\nInformación del libro:", info_libro)