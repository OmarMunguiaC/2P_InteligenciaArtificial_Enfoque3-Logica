class Tarea:
    def __init__(self, nombre, sub_tareas=None):
        self.nombre = nombre
        self.sub_tareas = sub_tareas if sub_tareas is not None else []

    def agregar_subtarea(self, sub_tarea):
        self.sub_tareas.append(sub_tarea)

    def __str__(self):
        return self.nombre

def imprimir_tareas(tarea, nivel=0):
    print("  " * nivel + tarea.nombre)
    for sub_tarea in tarea.sub_tareas:
        imprimir_tareas(sub_tarea, nivel + 1)

# Creamos las tareas
tarea_principal = Tarea("Tarea principal")
tarea_1 = Tarea("Tarea 1")
tarea_2 = Tarea("Tarea 2")
tarea_3 = Tarea("Tarea 3")
tarea_4 = Tarea("Tarea 4")
subtarea_1_1 = Tarea("Subtarea 1.1")
subtarea_1_2 = Tarea("Subtarea 1.2")
subtarea_2_1 = Tarea("Subtarea 2.1")
subtarea_2_2 = Tarea("Subtarea 2.2")
subtarea_3_1 = Tarea("Subtarea 3.1")
subtarea_3_2 = Tarea("Subtarea 3.2")
subtarea_4_1 = Tarea("Subtarea 4.1")
subtarea_4_2 = Tarea("Subtarea 4.2")

# Configuramos las relaciones jerárquicas
tarea_principal.agregar_subtarea(tarea_1)
tarea_principal.agregar_subtarea(tarea_2)
tarea_principal.agregar_subtarea(tarea_3)
tarea_principal.agregar_subtarea(tarea_4)
tarea_1.agregar_subtarea(subtarea_1_1)
tarea_1.agregar_subtarea(subtarea_1_2)
tarea_2.agregar_subtarea(subtarea_2_1)
tarea_2.agregar_subtarea(subtarea_2_2)
tarea_3.agregar_subtarea(subtarea_3_1)
tarea_3.agregar_subtarea(subtarea_3_2)
tarea_4.agregar_subtarea(subtarea_4_1)
tarea_4.agregar_subtarea(subtarea_4_2)

# Imprimimos la jerarquía de tareas
print("Jerarquía de tareas:")
imprimir_tareas(tarea_principal)
