import itertools

def equivalencia(exp1, exp2):
    # Genera todas las combinaciones de valores de verdad para p y q
    truth_values = [True, False]
    # Itera sobre todas las combinaciones de valores de verdad
    for p in truth_values:
        for q in truth_values:
            # Evalúa las expresiones con los valores de verdad actuales de p y q
            eval_exp1 = eval(exp1, {'p': p, 'q': q})
            eval_exp2 = eval(exp2, {'p': p, 'q': q})
            # Si las expresiones no son equivalentes, retorna False
            if eval_exp1 != eval_exp2:
                return False
    # Si las expresiones son equivalentes para todas las combinaciones, retorna True
    return True

def validez(exp):
    # Genera todas las combinaciones de valores de verdad para p y q
    truth_values = [True, False]
    # Itera sobre todas las combinaciones de valores de verdad
    for p in truth_values:
        for q in truth_values:
            # Si alguna combinación de valores de verdad hace que la expresión sea falsa, retorna False
            if not eval(exp, {'p': p, 'q': q}):
                return False
    # Si la expresión es verdadera para todas las combinaciones, retorna True
    return True

def satisfacibilidad(exp):
    # Genera todas las combinaciones de valores de verdad para p y q
    truth_values = [True, False]
    # Itera sobre todas las combinaciones de valores de verdad
    for p in truth_values:
        for q in truth_values:
            # Si alguna combinación de valores de verdad hace que la expresión sea verdadera, retorna True
            if eval(exp, {'p': p, 'q': q}):
                return True
    # Si no hay ninguna combinación de valores de verdad que haga que la expresión sea verdadera, retorna False
    return False

# Ejemplo de uso
exp1 = "(p and q) or (not p and not q)"
exp2 = "(p or q) and (not p or not q)"

# Imprime los resultados de las pruebas
print("Equivalencia:", equivalencia(exp1, exp2))
print("Validez:", validez(exp1))
print("Satisfacibilidad:", satisfacibilidad(exp1))
