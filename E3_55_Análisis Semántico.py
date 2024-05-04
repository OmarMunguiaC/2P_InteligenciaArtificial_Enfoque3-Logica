class AnalizadorSemantico:
    def __init__(self, arbol_sintactico):
        self.arbol_sintactico = arbol_sintactico
        self.variables = {}

    def analizar(self):
        try:
            self.validar_arbol(self.arbol_sintactico)
            print("Análisis semántico completado sin errores.")
        except Exception as e:
            print("Error semántico:", e)

    def validar_arbol(self, nodo):
        if nodo.tipo == "declaracion_variable":
            variable = nodo.hijos[0].valor
            valor = int(nodo.hijos[1].valor)
            if variable in self.variables:
                raise Exception(f"La variable '{variable}' ya ha sido declarada.")
            self.variables[variable] = valor
        elif nodo.tipo == "asignacion":
            variable = nodo.hijos[0].valor
            if variable not in self.variables:
                raise Exception(f"La variable '{variable}' no ha sido declarada.")
            valor = self.validar_expresion(nodo.hijos[1])
            self.variables[variable] = valor

    def validar_expresion(self, nodo):
        if nodo.tipo == "ID":
            variable = nodo.valor
            if variable not in self.variables:
                raise Exception(f"La variable '{variable}' no ha sido declarada.")
            return self.variables[variable]
        elif nodo.tipo == "NUM":
            return int(nodo.valor)
        elif nodo.tipo == "OPERADOR":
            izquierda = self.validar_expresion(nodo.hijos[0])
            derecha = self.validar_expresion(nodo.hijos[1])
            if nodo.valor == "+":
                return izquierda + derecha
            elif nodo.valor == "-":
                return izquierda - derecha

# Ejemplo de uso
class Nodo:
    def __init__(self, tipo, valor=None, hijos=None):
        self.tipo = tipo
        self.valor = valor
        self.hijos = hijos if hijos else []

arbol_sintactico = Nodo("programa", hijos=[
    Nodo("declaracion_variable", hijos=[
        Nodo("ID", "x"),
        Nodo("NUM", "10")
    ]),
    Nodo("asignacion", hijos=[
        Nodo("ID", "x"),
        Nodo("OPERADOR", "+", hijos=[
            Nodo("ID", "x"),
            Nodo("NUM", "5")
        ])
    ])
])

analizador = AnalizadorSemantico(arbol_sintactico)
analizador.analizar()
