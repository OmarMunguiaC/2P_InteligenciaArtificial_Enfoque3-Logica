class AnalizadorLexico:
    def __init__(self, entrada):
        self.entrada = entrada
        self.tokens = []

    def analizar(self):
        lexema = ""
        estado = 0

        for char in self.entrada:
            if estado == 0:
                if char.isalpha():  # Si el caracter es una letra
                    lexema += char
                    estado = 1
                elif char.isdigit():  # Si el caracter es un dígito
                    lexema += char
                    estado = 2
                elif char.isspace():  # Si el caracter es un espacio en blanco
                    estado = 0
                else:
                    self.tokens.append((char, char))  # Agregar token para operadores y otros símbolos
            elif estado == 1:
                if char.isalpha() or char.isdigit():  # Si el caracter es una letra o dígito
                    lexema += char
                else:
                    self.tokens.append(("ID", lexema))  # Agregar token para identificadores
                    lexema = ""
                    estado = 0
            elif estado == 2:
                if char.isdigit():  # Si el caracter es un dígito
                    lexema += char
                else:
                    self.tokens.append(("NUM", lexema))  # Agregar token para números
                    lexema = ""
                    estado = 0

        # Manejar el caso en el que el lexema final no se haya completado
        if estado == 1:
            self.tokens.append(("ID", lexema))
        elif estado == 2:
            self.tokens.append(("NUM", lexema))

# Ejemplo de uso
entrada = "int x = 42 + y;"
analizador = AnalizadorLexico(entrada)
analizador.analizar()
print("Tokens generados:")
for token in analizador.tokens:
    print(token)
