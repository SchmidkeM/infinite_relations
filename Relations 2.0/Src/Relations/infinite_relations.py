import sys
from .relation_schema import RelationSchema
from .relation import Relation

class AddRelation(Relation):
    def __init__(self):
        super().__init__(RelationSchema(["x", "y", "sum"]))

    def can_be_infinite(self):
        return True

    def can_is_member_loop(self):
        return False

    def members(self):
        for i in range(sys.maxsize):
            for j in range(i):
                yield [j, i-j, i]

    def is_member(self, element):
        return element[0] + element[1] == element[2]

    def print(self):
        super(AddRelation, self).print()
        
        members = self.members()
        while True:
            try:
                print(next(members))
            except StopIteration:
                return