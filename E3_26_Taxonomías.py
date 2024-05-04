class Categoria:
    def __init__(self, nombre, subcategorias=None):
        self.nombre = nombre
        self.subcategorias = subcategorias if subcategorias else []

    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)

    def __str__(self):
        return self.nombre

class Objeto:
    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria

    def __str__(self):
        return f"{self.nombre} ({self.categoria})"

# Definimos las categorías
animal = Categoria("Animal")
mamifero = Categoria("Mamífero")
reptil = Categoria("Reptil")
ave = Categoria("Ave")

# Definimos los objetos
perro = Objeto("Perro", mamifero)
gato = Objeto("Gato", mamifero)
iguana = Objeto("Iguana", reptil)
aguila = Objeto("Águila", ave)

# Agregamos subcategorías
animal.agregar_subcategoria(mamifero)
animal.agregar_subcategoria(reptil)
animal.agregar_subcategoria(ave)

# Mostramos la taxonomía
print("Taxonomía:")
print(animal)
for subcategoria in animal.subcategorias:
    print(f"- {subcategoria}")
    for objeto in subcategoria.subcategorias:
        print(f"  * {objeto}")
