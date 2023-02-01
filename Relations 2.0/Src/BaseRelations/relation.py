from __future__ import annotations
from abc import ABC, abstractclassmethod
from .relation_schema import RelationSchema

# obecná relace, abstraktní třída
class Relation(ABC):

    def __init__(self, schema: RelationSchema):
        self.schema: RelationSchema = schema

    @abstractclassmethod
    def can_be_infinite(self):
        pass

    @abstractclassmethod
    def can_is_member_loop(self):
        pass

    @abstractclassmethod
    def is_member(self, element):
        pass
    
    @abstractclassmethod
    def members(self):
        pass

    def print(self):
        self.schema.print()
