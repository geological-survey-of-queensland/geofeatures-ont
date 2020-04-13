import requests

URIS = [
    {
        "uri": "http://localhost/def/geofeatures",
        "params": {},
        "headers": {},
        "test": "<title>Geologic Features Ontology</title>"
    },
    {
        "uri": "http://localhost/def/geofeatures",
        "params": "_mediatype=text/turtle",
        "headers": {},
        "test": 'skos:prefLabel "Geologic Features Ontology"@en ;'
    },
    {
        "uri": "http://localhost/def/geofeatures",
        "params": "",
        "headers": {"Accept": "text/turtle"},
        "test": 'skos:prefLabel "Geologic Features Ontology"@en ;'
    },
    {
        "uri": "http://localhost/def/geofeatures.ttl",
        "params": {},
        "headers": {},
        "test": 'skos:prefLabel "Geologic Features Ontology"@en ;'
    },
    {
        "uri": "http://localhost/def/geofeatures",
        "params": "_profile=alt",
        "headers": {},
        "test": "Alternate Profiles of the Geologic Features Ontology"
    },
    {
        "uri": "http://localhost/def/geofeatures",
        "params": "_profile=alt&_mediatype=text/turtle",
        "headers": {},
        "test": 'altr:hasRepresentation _:rep-1 , _:rep-2 , _:rep-3 , _:rep-4 ;'
    },
    {
        "uri": "http://localhost/def/geofeatures",
        "params": "_profile=alt",
        "headers": {"Accept": "text/turtle"},
        "test": 'altr:hasRepresentation _:rep-1 , _:rep-2 , _:rep-3 , _:rep-4 ;'
    },
    {
        "uri": "http://localhost/def/geofeatures.ttl",
        "params": "_profile=alt",
        "headers": {},
        "test": 'altr:hasRepresentation _:rep-1 , _:rep-2 , _:rep-3 , _:rep-4 ;'
    },
    {
        "uri": "http://localhost/def/geofeatures",
        "params": "_profile=http://www.w3.org/ns/dx/conneg/altr",
        "headers": {},
        "test": "Alternate Profiles of the Geologic Features Ontology"
    },
    {
        "uri": "http://localhost/def/geofeatures",
        "params": "_profile=http://www.w3.org/ns/dx/conneg/altr&_mediatype=text/turtle",
        "headers": {},
        "test": 'altr:hasRepresentation _:rep-1 , _:rep-2 , _:rep-3 , _:rep-4 ;'
    },
    {
        "uri": "http://localhost/def/geofeatures",
        "params": "_profile=http://www.w3.org/ns/dx/conneg/altr",
        "headers": {"Accept": "text/turtle"},
        "test": 'altr:hasRepresentation _:rep-1 , _:rep-2 , _:rep-3 , _:rep-4 ;'
    },
    {
        "uri": "http://localhost/def/geofeatures.ttl",
        "params": "_profile=http://www.w3.org/ns/dx/conneg/altr",
        "headers": {},
        "test": 'altr:hasRepresentation _:rep-1 , _:rep-2 , _:rep-3 , _:rep-4 ;'
    },
    {
        "uri": "http://localhost/def/geofeatures",
        "params": "",
        "headers": {"Accept-Profile": "<http://www.w3.org/ns/dx/conneg/altr>"},
        "test": "Alternate Profiles of the Geologic Features Ontology"
    },
    {
        "uri": "http://localhost/def/geofeatures",
        "params": "_mediatype=text/turtle",
        "headers": {"Accept-Profile": "<http://www.w3.org/ns/dx/conneg/altr>"},
        "test": 'altr:hasRepresentation _:rep-1 , _:rep-2 , _:rep-3 , _:rep-4 ;'
    },
    {
        "uri": "http://localhost/def/geofeatures",
        "params": "",
        "headers": {"Accept-Profile": "<http://www.w3.org/ns/dx/conneg/altr>", "Accept": "text/turtle"},
        "test": 'altr:hasRepresentation _:rep-1 , _:rep-2 , _:rep-3 , _:rep-4 ;'
    },
    {
        "uri": "http://localhost/def/geofeatures.ttl",
        "params": "",
        "headers": {"Accept-Profile": "<http://www.w3.org/ns/dx/conneg/altr>"},
        "test": 'altr:hasRepresentation _:rep-1 , _:rep-2 , _:rep-3 , _:rep-4 ;'
    },
    {
        "uri": "http://localhost/def/geofeatures",
        "params": "_profile=skos",
        "headers": {},
        "test": "<h1>Vocabulary: Geologic Feature Types</h1>"
    },
    {
        "uri": "http://localhost/def/geofeatures",
        "params": "_profile=skos&_mediatype=text/turtle",
        "headers": {},
        "test": 'skos:prefLabel "Geologic Feature Types" .'
    },
    {
        "uri": "http://localhost/def/geofeatures",
        "params": "_profile=skos",
        "headers": {"Accept": "text/turtle"},
        "test": 'skos:prefLabel "Geologic Feature Types" .'
    },
    {
        "uri": "http://localhost/def/geofeatures.ttl",
        "params": "_profile=skos",
        "headers": {},
        "test": 'skos:prefLabel "Geologic Feature Types" .'
    },
    {
        "uri": "http://localhost/def/geofeatures",
        "params": "_profile=https://www.w3.org/TR/skos-reference/",
        "headers": {},
        "test": "<h1>Vocabulary: Geologic Feature Types</h1>"
    },
    {
        "uri": "http://localhost/def/geofeatures",
        "params": "_profile=https://www.w3.org/TR/skos-reference/&_mediatype=text/turtle",
        "headers": {},
        "test": 'skos:prefLabel "Geologic Feature Types" .'
    },
    {
        "uri": "http://localhost/def/geofeatures",
        "params": "_profile=https://www.w3.org/TR/skos-reference/",
        "headers": {"Accept": "text/turtle"},
        "test": 'skos:prefLabel "Geologic Feature Types" .'
    },
    {
        "uri": "http://localhost/def/geofeatures.ttl",
        "params": "_profile=https://www.w3.org/TR/skos-reference/",
        "headers": {},
        "test": 'skos:prefLabel "Geologic Feature Types" .'
    },
    # {
    #     "uri": "http://localhost/def/geofeatures",
    #     "params": "",
    #     "headers": {"Accept-Profile": "<https://www.w3.org/TR/skos-reference/>"},
    #     "test": "<h1>Vocabulary: Geologic Feature Types</h1>"
    # },
    # {
    #     "uri": "http://localhost/def/geofeatures",
    #     "params": "_mediatype=text/turtle",
    #     "headers": {"Accept-Profile": "<https://www.w3.org/TR/skos-reference/>"},
    #     "test": 'skos:prefLabel "Geologic Feature Types" .'
    # },
    # {
    #     "uri": "http://localhost/def/geofeatures",
    #     "params": "",
    #     "headers": {"Accept-Profile": "<https://www.w3.org/TR/skos-reference/>", "Accept": "text/turtle"},
    #     "test": 'skos:prefLabel "Geologic Feature Types" .'
    # },
    # {
    #     "uri": "http://localhost/def/geofeatures.ttl",
    #     "params": "",
    #     "headers": {"Accept-Profile": "<https://www.w3.org/TR/skos-reference/>"},
    #     "test": 'skos:prefLabel "Geologic Feature Types" .'
    # },
]
for URI in URIS:
    print(
        "testing: {}{}{}".format(
            URI["uri"],
            "?" + URI["params"] if len(URI["params"]) > 0 else '',
            " " + str(URI["headers"]) if URI["headers"] is not None else ""
        )
    )
    r = requests.get(
        URI["uri"],
        params=URI["params"],
        headers=URI["headers"],
        allow_redirects=True
    )
    # print(r.text)
    assert URI["test"] in r.text

