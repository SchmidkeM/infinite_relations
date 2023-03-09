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
                yield self.create_tuple([j, i-j, i])
            i += 1

    def is_member(self, element: dict):
        vals = list(element.values())
        return vals[0] + vals[1] == vals[2]


class NaturalNumbersRelation(Relation):
    def __init__(self, schema: RelationSchema = RelationSchema(["n"])):
        if len(schema) == 1:
            super().__init__(schema)
        else:
            raise Exception("Schema of NaturalNumbersRelation must have 1 attribute")

    def can_be_infinite(self):
        return True

    def can_is_member_loop(self):
        return False

    def members(self):
        i = 0
        while True:
            yield self.create_tuple([i])
            i += 1

    def is_member(self, element: dict):
        vals = list(element.values())
        if len(vals) == 1:
            val = vals[0]
            return isinstance(val, int) and val >= 0
        return False