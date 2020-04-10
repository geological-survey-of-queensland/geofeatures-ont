import rdflib

# original ont graph
g = rdflib.Graph().parse("../geofeatures.ttl", format="turtle")

# vocab graph
g_skos = rdflib.Graph()
g_skos.bind('skos', rdflib.namespace.SKOS)
g_skos.bind('dcterms', rdflib.namespace.DCTERMS)
g_skos.bind('prof', rdflib.Namespace("http://www.w3.org/ns/dx/prof/"))
g_skos.bind('owl', rdflib.Namespace("http://www.w3.org/2002/07/owl#"))
g_skos.bind('sdo', rdflib.Namespace("https://schema.org/"))
g_skos.bind('geof', rdflib.Namespace("http://linked.data.gov.au/def/geofeatures/"))

# get Classes as Concepts
q = """
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dcterms: <http://purl.org/dc/terms/>
CONSTRUCT {
    ?s a skos:Concept ;
        skos:prefLabel ?pl ;
        skos:definition ?def ;
        skos:inScheme ?cs ;
        skos:notation ?n .

    ?s skos:broader ?s2 ;
       dcterms:source ?source .
}
WHERE {
    ?cs a owl:Ontology .

    ?s a owl:Class ;
        skos:prefLabel ?pl ;
        skos:definition ?def .

    OPTIONAL {
        ?s rdfs:subClassOf ?s2 ;
           dcterms:source ?source ;
           skos:notation ?n .
    }
}
"""
g_skos += g.query(q)

# get Ontology as a ConceptScheme
q = """
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
CONSTRUCT {
    ?s a owl:Ontology , skos:ConceptScheme .
    ?s ?p ?o .
}
WHERE {
    ?s a owl:Ontology .
    ?s ?p ?o .
}
"""
g_skos += g.query(q)

# add any class without a local subClassOf as a hasTopConcept
q = """
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX sdo: <https://schema.org/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
CONSTRUCT {
    ?cs skos:hasTopConcept ?s .
}
WHERE {
    ?cs a owl:Ontology .
    ?s a owl:Class .
    
    FILTER NOT EXISTS {?s rdfs:subClassOf ?z}
}
"""
g_skos += g.query(q)

# get Agents - Persons
q = """
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX sdo: <https://schema.org/>
CONSTRUCT {
    ?s ?p ?o .
}
WHERE {
    ?s a sdo:Person .
    ?s ?p ?o .
}
"""
g_skos += g.query(q)

# get Agents - Organizations
q = """
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX sdo: <https://schema.org/>
CONSTRUCT {
    ?s ?p ?o .
}
WHERE {
    ?s a sdo:Organization .
    ?s ?p ?o .
}
"""
g_skos += g.query(q)

with open("../geologic-feature-types.ttl", "w") as f:
    f.write(g_skos.serialize(format="turtle").decode("utf-8"))