class SistemaDiagnostico:
    def __init__(self, reglas):
        self.reglas = reglas

    def diagnosticar(self, sintomas):
        """
        Realiza el diagnóstico basado en los síntomas proporcionados.
        """
        diagnosticos = set()
        for regla, diagnostico in self.reglas.items():
            if all(sintoma in sintomas for sintoma in regla):
                diagnosticos.add(diagnostico)
        return diagnosticos

reglas_diagnosticos = {
    ('fiebre', 'tos'): 'Gripe',
    ('dolor_de_garganta', 'fatiga'): 'Resfriado',
    ('dolor_de_cabeza', 'fiebre', 'fatiga'): 'Migraña',
    ('dolor_de_garganta', 'fiebre'): 'Amigdalitis'
}
sistema_diagnostico = SistemaDiagnostico(reglas_diagnosticos)

# Síntomas del paciente
sintomas_paciente = ['fiebre', 'fatiga']

# Realizar diagnóstico
diagnosticos = sistema_diagnostico.diagnosticar(sintomas_paciente)
print("Diagnósticos posibles:", diagnosticos)
