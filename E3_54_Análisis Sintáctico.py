class AnalizadorSintactico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.posicion = 0
        self.error = False

    def analizar(self):
        try:
            self.programa()
            if not self.error and self.posicion == len(self.tokens):
                print("Análisis sintáctico completado sin errores.")
            else:
                print("Error sintáctico.")
        except Exception as e:
            print("Error:", e)

    def emparejar(self, tipo_esperado):
        if self.posicion < len(self.tokens) and self.tokens[self.posicion][0] == tipo_esperado:
            self.posicion += 1
        else:
            self.error = True
            raise Exception(f"Se esperaba un token de tipo '{tipo_esperado}' pero se encontró '{self.tokens[self.posicion][0]}' en la posición {self.posicion}.")

    def programa(self):
        self.declaracion_variable()
        self.asignacion()
        self.expresion()

    def declaracion_variable(self):
        self.emparejar("ID")
        self.emparejar("ASIGNACION")
        self.emparejar("NUM")
        self.emparejar("PUNTO_COMA")

    def asignacion(self):
        self.emparejar("ID")
        self.emparejar("ASIGNACION")
        self.expresion()
        self.emparejar("PUNTO_COMA")

    def expresion(self):
        self.emparejar("ID")
        self.emparejar("OPERADOR")
        self.emparejar("ID")

# Ejemplo de uso
tokens = [
    ("ID", "x"),
    ("ASIGNACION", "="),
    ("NUM", "42"),
    ("PUNTO_COMA", ";"),
    ("ID", "y"),
    ("ASIGNACION", "="),
    ("ID", "x"),
    ("OPERADOR", "+"),
    ("NUM", "2"),
    ("PUNTO_COMA", ";")
]

analizador = AnalizadorSintactico(tokens)
analizador.analizar()
