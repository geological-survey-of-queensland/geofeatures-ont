<img src="style/gsq.jpg" style="width:25%" />  

# SWEET Geological Features Profile Ontology
This ontology describes classes of geological and administrative Feature relevant to the duties of the Geological Survey of Queensland.

As subclasses of the GeoSPARQL Ontology's `Feature` class, this ontology defines `Geological Feature` and `Administrative Feature`. Multiple subclasses of those two main classes are also defined.

Most of the subclasses of `Geological Feature` defined here are not disjoint with other subclasses of it in recognition of the fact that a real-world Feature may be classed in multiple ways. `Administrative Feature` subclasses, however, are all disjoint having been defined disjointly by people.

References to and positioning of other Features defined elsewhere are made, such as placing the HY_Features model's `Catchment` and `CatchmentAggregate` classes as subclasses of this ontology's `Basin` class (a subclass of `Geological Feature`). As a result, the classes of object within the LocI project's [Geofabric dataset](http://linked.data.gov.au/dataset/geofabric))can be related to objects classified using this ontology.

## Online
This ontology will soon be visible online at its namespace URI location:

* <http://linked.data.gov.au/def/sweetgeofeatures>


## Repository Contents
This repository contains both the machine-readable ontology file in the RDF Turtle format, [sweetgeofeatures.ttl](sweetgeofeatures.ttl), and an HTML web page version of it for people to use [sweetgeofeatures.html](sweetgeofeatures.html). The HTML web page is generated semi-automatically from the RDF file and will soon be displayed online at this ontology's namespace location indicated above.


## License
The content of this API is licensed for use under the [Creative Commons 4.0 License](https://creativecommons.org/licenses/by/4.0/). See the [license deed](LICENSE) all details.


## Citation
If you wish to cite this profile, please do so like this:

Geological Survey of Queensland (2019) "Geo-Admin Features Ontology". An OWL ontology defining classes of geospatial Feature relevant to the duties of the Geological Survey of Queensland. http://linked.data.gov.au/def/gsq-features


## Contacts
*owner*:  
**Geological Survey of Queensland**  
*Within the Queensland Department of Natural Resources, Mines & Energy*  
1 William St, Brisbane, Queensland, Australia  
<https://www.business.qld.gov.au/industries/mining-energy-water/resources/geoscience-information/gsq>  
<GSQOpenData@dnrme.qld.gov.au>  

*author*:  
**Nicholas Car**  
[SURROUND Australia Pty Ltd](https://surroundaustralia.com)  
<nicholas.car@surroundaustralia.com>  
<http://orcid.org/0000-0002-8742-7730>  
