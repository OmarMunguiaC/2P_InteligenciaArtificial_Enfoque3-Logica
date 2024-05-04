def truth_table(expression):
    variables = sorted(set([char for char in expression if char.isalpha()]))
    num_vars = len(variables)
    print(" | ".join(variables) + " | " + expression)
    print("-" * (num_vars * 3 + len(expression) + 1))

    for i in range(2 ** num_vars):
        assignment = [int(x) for x in bin(i)[2:].zfill(num_vars)]
        var_map = dict(zip(variables, assignment))
        eval_exp = eval(expression, var_map)
        truth_values = [str(val) for val in assignment] + [str(int(eval_exp))]
        print(" | ".join(truth_values))

# Ejemplo de uso
expression = "(A and B) or (C and not D)"
truth_table(expression)
