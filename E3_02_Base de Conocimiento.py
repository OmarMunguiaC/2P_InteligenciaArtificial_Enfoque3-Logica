knowledge_base = {
    'Padres': ['Juan', 'María'],
    'Hijos': {
        'Juan': ['Pedro', 'Ana'],
        'María': ['Luis']
    },
    'Edades': {
        'Juan': 40,
        'María': 38,
        'Pedro': 20,
        'Ana': 18,
        'Luis': 10
    }
}

# Consulta en la base de conocimiento
def consulta_edad(nombre):
    return knowledge_base['Edades'].get(nombre, "Desconocido")

# Ejemplo de uso
nombre = 'Pedro'
print(f"La edad de {nombre} es {consulta_edad(nombre)} años.")
