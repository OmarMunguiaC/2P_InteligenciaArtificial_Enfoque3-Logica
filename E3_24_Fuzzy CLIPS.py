import clips

# Crea un nuevo entorno CLIPS
env = clips.Environment()

# Carga el módulo de lógica difusa
env.load("fuzzy.clp")

# Activa el módulo de lógica difusa
env.run()

# Agrega una regla difusa
env.assert_string("(fuzzy-rule (if (temperatura is cold) (humidity is high)) (then (comfort is poor)))")

# Inserta hechos difusos
env.assert_string("(temperatura 25)")
env.assert_string("(humidity 0.8)")

# Realiza inferencia difusa
env.run()

# Recupera el resultado de la inferencia
for fact in env.facts():
    print(fact)
