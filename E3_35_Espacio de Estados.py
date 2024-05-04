class Estado:
    def __init__(self, nombre, acciones_posibles):
        self.nombre = nombre
        self.acciones_posibles = acciones_posibles

    def __str__(self):
        return self.nombre

class Accion:
    def __init__(self, nombre, estado_siguiente):
        self.nombre = nombre
        self.estado_siguiente = estado_siguiente

# Definimos los estados y acciones
estado_a = Estado("Estado A", ["A -> B", "A -> C"])
estado_b = Estado("Estado B", ["B -> C", "B -> D"])
estado_c = Estado("Estado C", ["C -> D"])
estado_d = Estado("Estado D", [])

accion_ab = Accion("A -> B", estado_b)
accion_ac = Accion("A -> C", estado_c)
accion_bc = Accion("B -> C", estado_c)
accion_bd = Accion("B -> D", estado_d)
accion_cd = Accion("C -> D", estado_d)

# Creamos un diccionario que mapea el nombre de cada estado a su objeto Estado
estados = {
    "A": estado_a,
    "B": estado_b,
    "C": estado_c,
    "D": estado_d
}

# Creamos un diccionario que mapea el nombre de cada acción a su objeto Accion
acciones = {
    "A -> B": accion_ab,
    "A -> C": accion_ac,
    "B -> C": accion_bc,
    "B -> D": accion_bd,
    "C -> D": accion_cd
}

# Función para mostrar el espacio de estados
def mostrar_espacio_estados():
    print("Espacio de Estados:")
    for nombre, estado in estados.items():
        print(f"{nombre}: {', '.join(estado.acciones_posibles)}")

# Función para obtener el estado siguiente dado un estado y una acción
def obtener_estado_siguiente(estado_actual, accion):
    if accion in estado_actual.acciones_posibles:
        return acciones[accion].estado_siguiente
    else:
        return None

# Mostramos el espacio de estados
mostrar_espacio_estados()

# Ejemplo de cómo obtener el estado siguiente
estado_actual = estado_a
accion_elegida = "A -> B"
estado_siguiente = obtener_estado_siguiente(estado_actual, accion_elegida)

if estado_siguiente:
    print(f"Si estamos en {estado_actual}, y elegimos la acción {accion_elegida}, llegaremos a {estado_siguiente}.")
else:
    print(f"No se puede ejecutar la acción {accion_elegida} desde el estado {estado_actual}.")
