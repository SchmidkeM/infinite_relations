from __future__ import annotations
from .relation_schema import RelationSchema
from .relation import Relation


class ListRelation(Relation):

    def __init__(self, schema: RelationSchema, tuples: list = []):
        super(ListRelation, self).__init__(schema)
        self.tuples = tuples

    def can_be_infinite(self):
        return False

    def can_is_member_loop(self):

        return False

    def members(self):
        return iter(self.tuples)

    def is_member(self, tuple):
        return tuple in self.tuples

    def print(self):
        super(ListRelation, self).print()
        for tuple in self.tuples:
            print(tuple)
