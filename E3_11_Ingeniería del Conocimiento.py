class SistemaRecomendacionPeliculas:
    def __init__(self, conocimiento):
        self.conocimiento = conocimiento

    def recomendar_pelicula(self, preferencias_usuario):
        """
        Recomienda una película basada en las preferencias del usuario.
        """
        recomendaciones = []
        for regla, pelicula in self.conocimiento.items():
            if all(pref in preferencias_usuario for pref in regla):
                recomendaciones.append(pelicula)
        return recomendaciones

conocimiento_recomendacion = {
    ('accion', 'aventura'): 'Indiana Jones',
    ('comedia', 'romance'): 'Amelie',
    ('drama',): 'El Padrino',
    ('animacion',): 'Toy Story'
}
sistema_recomendacion = SistemaRecomendacionPeliculas(conocimiento_recomendacion)

# Preferencias del usuario
preferencias_usuario = ['accion', 'aventura']

# Realizar recomendación
recomendaciones = sistema_recomendacion.recomendar_pelicula(preferencias_usuario)
print("Películas recomendadas:", recomendaciones)
