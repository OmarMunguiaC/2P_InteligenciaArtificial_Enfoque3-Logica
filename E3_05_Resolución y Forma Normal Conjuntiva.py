from sympy import symbols, Or, And, Not, to_cnf, satisfiable, ask

def resolucion_FNC(expresion):
    # Convierte la expresión a la Forma Normal Conjuntiva (FNC)
    FNC = to_cnf(expresion)
    # Imprime la expresión en FNC
    print("Expresión en Forma Normal Conjuntiva (FNC):", FNC)

    # Realiza la resolución sobre la expresión en FNC
    resultado = ask(FNC, 'valid')
    # Si la expresión es válida, devuelve True, de lo contrario False
    return resultado

# Ejemplo de uso
p, q, r = symbols('p q r')
expresion = Or(And(p, q), And(Not(p), r), Not(r))

# Verifica la validez de la expresión en FNC utilizando el método de resolución
resultado = resolucion_FNC(expresion)
print("Validez de la expresión en FNC:", resultado)
