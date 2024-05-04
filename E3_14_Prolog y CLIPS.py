# Prolog-style
class PrologHermanos:
    def __init__(self):
        self.relaciones = [
            ('juan', 'maria'),
            ('juan', 'pedro'),
            ('maria', 'juan'),
            ('maria', 'pedro'),
            ('pedro', 'juan'),
            ('pedro', 'maria')
        ]

    def hermano(self, x, y):
        return (x, y) in self.relaciones or (y, x) in self.relaciones

# CLIPS-style
class ClipsHermanos:
    def __init__(self):
        self.relaciones = [
            ('juan', 'maria'),
            ('juan', 'pedro'),
            ('maria', 'juan'),
            ('maria', 'pedro'),
            ('pedro', 'juan'),
            ('pedro', 'maria')
        ]

    def hermano(self, x, y):
        return any((x, y) in self.relaciones or (y, x) in self.relaciones for x, y in self.relaciones)

# Uso de los dos estilos
nombre1 = 'juan'
nombre2 = 'maria'

prolog = PrologHermanos()
es_hermano_prolog = prolog.hermano(nombre1, nombre2)
print(f"¿{nombre1} y {nombre2} son hermanos? (Prolog-style): {es_hermano_prolog}")

clips = ClipsHermanos()
es_hermano_clips = clips.hermano(nombre1, nombre2)
print(f"¿{nombre1} y {nombre2} son hermanos? (CLIPS-style): {es_hermano_clips}")
