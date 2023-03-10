from __future__ import annotations
from abc import ABC, abstractclassmethod
from .relation_schema import RelationSchema

# obecná relace, abstraktní třída
class Relation(ABC):

    def __init__(self, schema: RelationSchema):
        self.__schema__: RelationSchema = schema

    def schema(self):
        return self.__schema__
    
    def attributes(self):
        return self.schema().attribute_list

    def can_be_infinite(self):
        True

    def can_is_member_loop(self):
        True
    
    @abstractclassmethod
    def members(self):
        pass

    def is_member(self, tuple: dict):
        return tuple in self.members()

    def print(self, limit: int = 10_000):
        print("============")
        self.schema().print()
        print("------------")
        for tuple in self.members():
            print(*tuple.values())
            limit -= 1
            if limit == 0:
                break
        print("============")

    def create_tuple(self, values: list):
        return self.schema().__create_tuple__(values)
