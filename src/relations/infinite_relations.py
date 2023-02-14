import sys
from .relation_schema import RelationSchema
from .relation import Relation

class AddRelation(Relation):
    def __init__(self, schema: RelationSchema = RelationSchema(["x", "y", "sum"])):
        if len(schema) == 3:
            super().__init__(schema)
        else:
            Exception("Schema of AddRelation must have 3 attributes")

    def can_be_infinite(self):
        return True

    def can_is_member_loop(self):
        return False

    def members(self):
        for i in range(sys.maxsize):
            for j in range(i+1):
                yield [j, i-j, i]

    def is_member(self, element):
        return element[0] + element[1] == element[2]
