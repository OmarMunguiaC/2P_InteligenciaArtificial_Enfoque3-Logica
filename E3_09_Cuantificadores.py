from sympy import symbols, forall, exists

# Definir símbolos
x, y = symbols('x y')

# Ejemplo de cuantificador universal (∀)
# ∀x (x > 0)
prop_universal = forall(x, x > 0)
print("¿Para todo x, x es mayor que 0?", prop_universal)

# Ejemplo de cuantificador existencial (∃)
# ∃y (y < 0)
prop_existencial = exists(y, y < 0)
print("¿Existe algún y que sea menor que 0?", prop_existencial)
