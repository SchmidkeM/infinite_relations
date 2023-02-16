from __future__ import annotations
from abc import ABC, abstractclassmethod
from ..relations.relation_schema import RelationSchema
from ..relations.relation import Relation

# předek pro binární operace relační algebry, abstraktní třída
class BinaryOperation(Relation):
    def __init__(self, schema: RelationSchema, left: Relation, right: Relation):
        super().__init__(schema)
        self.__left__ = left
        self.__right__ = right

    def left(self):
        return self.__left__
    
    def right(self):
        return self.__right__
