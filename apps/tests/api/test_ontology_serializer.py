from api.ontology_serializer import serialize_entity_tree
from semantic import OntologyLoader

onto = OntologyLoader.load_from_path("./tests/test_data/test-ontology.rdf")

class TestTreeSerialization:

    def test_ontology_serializer(self):
        result = serialize_entity_tree([ onto.AbstractionScope ])
        assert isinstance(result, list)
