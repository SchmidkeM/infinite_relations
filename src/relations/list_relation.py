from __future__ import annotations
from .relation_schema import RelationSchema
from .relation import Relation


class ListRelation(Relation):

    def __init__(self, schema: RelationSchema, tuples: list = []):
        super().__init__(schema)
        self.__tuples__ = tuples

    def can_be_infinite(self):
        return False

    def can_is_member_loop(self):
        return False

    def members(self):
        return iter(self.__tuples__)
