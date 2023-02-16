from .relation_schema import RelationSchema
from .relation import Relation
from ..utils import dict_from_lists

class AddRelation(Relation):
    def __init__(self, schema: RelationSchema = RelationSchema(["x", "y", "sum"])):
        if len(schema) == 3:
            super().__init__(schema)
        else:
            raise Exception("Schema of AddRelation must have 3 attributes")

    def can_be_infinite(self):
        return True

    def can_is_member_loop(self):
        return False

    def members(self):
        i = 0
        while True:
            for j in range(i+1):
                yield dict_from_lists(self.schema().attribute_list, [j, i-j, i])
            i += 1

    def is_member(self, element):
        return element[0] + element[1] == element[2]
