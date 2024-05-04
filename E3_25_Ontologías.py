from rdflib import Graph, Namespace, RDF, RDFS, Literal

# Creamos un grafo RDF
g = Graph()

# Definimos un namespace para nuestra ontología
onto = Namespace("http://example.org/ontology#")

# Definimos las clases
g.add((onto.Persona, RDF.type, RDFS.Class))
g.add((onto.Empleado, RDF.type, RDFS.Class))
g.add((onto.Estudiante, RDF.type, RDFS.Class))

# Definimos propiedades
g.add((onto.tieneNombre, RDF.type, RDF.Property))
g.add((onto.tieneEdad, RDF.type, RDF.Property))
g.add((onto.tieneTrabajo, RDF.type, RDF.Property))
g.add((onto.asisteA, RDF.type, RDF.Property))

# Definimos subclases
g.add((onto.Empleado, RDFS.subClassOf, onto.Persona))
g.add((onto.Estudiante, RDFS.subClassOf, onto.Persona))

# Agregamos instancias y relaciones
juan = onto.juan
g.add((juan, RDF.type, onto.Persona))
g.add((juan, onto.tieneNombre, Literal("Juan")))
g.add((juan, onto.tieneEdad, Literal(30)))

juan_empleado = onto.juan_empleado
g.add((juan_empleado, RDF.type, onto.Empleado))
g.add((juan_empleado, onto.tieneTrabajo, Literal("Ingeniero de software")))
g.add((juan, onto.asisteA, onto.UC3M))

# Guardamos el grafo en un archivo
g.serialize("ontologia.rdf", format="xml")
