from __future__ import annotations
from .relation_schema import RelationSchema
from .relation import Relation
from ..utils import compare_lists_orderless


class ListRelation(Relation):

    def __init__(self, schema: RelationSchema, tuples: list = []):
        if len(tuples) > 0:
            if len(schema) != len(tuples[0]):
                raise Exception("Length of schema and tuples must match")
            if not isinstance(tuples[0], dict):
                raise Exception("Tuples must be dictionaries")
        super().__init__(schema)
        self.__tuples__: list = tuples

    def can_be_infinite(self):
        return False

    def can_is_member_loop(self):
        return False

    def members(self):
        return iter(self.__tuples__)

    def insert(self, tuple: dict):
        if compare_lists_orderless(self.schema.attribute_list, tuple.keys()):
            self.__tuples__.append(tuple)
        else:
            raise Exception("Trying to insert wrong type tuple")