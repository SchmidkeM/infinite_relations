from __future__ import annotations
from ..relations.relation import Relation
from ..relations.relation_schema import RelationSchema
from .unary_operation import UnaryOperation

class Projection(UnaryOperation):
    def __init__(self, relation: Relation, new_schema: RelationSchema):
        if new_schema.is_subset_of(relation.schema()):
            super().__init__(relation)
            self.__new_schema__ = new_schema
        else:
            raise Exception("Schema of projection must be a subset of original schema")
        
    def members(self):
        for tuple in self.original_relation().members():
            yield {attr: tuple[attr] for attr in self.schema().attribute_list}
    
    def schema(self):
        return self.__new_schema__