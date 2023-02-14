from __future__ import annotations
from abc import ABC, abstractclassmethod
from .relation_schema import RelationSchema

# obecná relace, abstraktní třída
class Relation(ABC):

    def __init__(self, schema: RelationSchema):
        self.schema: RelationSchema = schema

    def can_be_infinite(self):
        True

    def can_is_member_loop(self):
        True
    
    @abstractclassmethod
    def members(self):
        pass

    def is_member(self, tuple):
        return tuple in self.members()

    def print(self, limit=10_000):
        self.schema.print()
        for tuple in self.members():
            print(tuple)
            limit -= 1
            if limit == 0:
                return
