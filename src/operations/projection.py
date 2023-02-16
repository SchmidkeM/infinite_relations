from __future__ import annotations
from ..relations.relation import Relation
from ..relations.relation_schema import RelationSchema
from .unary_operation import UnaryOperation

class Projection(UnaryOperation):
    def __init__(self, relation: Relation, new_schema: RelationSchema):
        if new_schema.is_subset_of(relation.schema):
            super().__init__(relation)
            self.new_schema = new_schema
        else:
            raise Exception("Schema of projection must be a subset of original schema")
        
    def members(self):
        for tuple in self.original_relation().members():
            yield {attr: tuple[attr] for attr in self.new_schema.attribute_list}
    
    # TODO: dát self.schema jako funkci aby se mohla overridnout místo celého printu (takhle je to hodně duplicitní, plus to ani nefunguje vždy)
    def print(self, limit: int = 10_000):
        print("============")
        self.new_schema.print()
        print("------------")
        for tuple in self.members():
            print(*tuple.values())
            limit -= 1
            if limit == 0:
                break
        print("============")