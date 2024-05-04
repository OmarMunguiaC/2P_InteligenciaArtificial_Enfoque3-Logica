from collections import defaultdict

def unificar(x, y, sustitucion=None):
    """
    Realiza unificación de dos términos.
    """
    if sustitucion is None:
        sustitucion = {}

    if x == y:
        return sustitucion

    if isinstance(x, str) and x.islower():
        return unificar_var(x, y, sustitucion)
    elif isinstance(y, str) and y.islower():
        return unificar_var(y, x, sustitucion)
    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            return None
        for x_i, y_i in zip(x, y):
            sustitucion = unificar(x_i, y_i, sustitucion)
            if sustitucion is None:
                return None
        return sustitucion
    else:
        return None

def unificar_var(var, x, sustitucion):
    """
    Unifica una variable con un término.
    """
    if var in sustitucion:
        return unificar(sustitucion[var], x, sustitucion)
    elif isinstance(x, str) and x.islower() and x in sustitucion:
        return unificar(var, sustitucion[x], sustitucion)
    elif occurs_check(var, x, sustitucion):
        return None
    else:
        sustitucion[var] = x
        return sustitucion

def occurs_check(var, x, sustitucion):
    """
    Verifica si una variable ocurre en un término.
    """
    if var == x:
        return True
    elif isinstance(x, str) and x.islower() and x in sustitucion:
        return occurs_check(var, sustitucion[x], sustitucion)
    elif isinstance(x, list):
        return any(occurs_check(var, term, sustitucion) for term in x)
    else:
        return False

# Ejemplo de uso
t1 = ['f', 'X', 'a']
t2 = ['f', 'b', 'Y']

sustitucion = unificar(t1, t2)
if sustitucion is not None:
    print("Unificación exitosa:")
    for var, valor in sustitucion.items():
        print(f"{var} = {valor}")
else:
    print("No se puede unificar los términos.")
