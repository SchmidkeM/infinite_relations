from ..relations.relation import Relation
from ..relations.relation_schema import RelationSchema

class UnaryOperation(Relation):
    def __init__(self, relation: Relation):
        super().__init__(relation.schema)
        self.__original_relation__ = relation

    def original_relation(self):
        return self.__original_relation__
    
    def can_be_infinite(self):
        return self.original_relation().can_be_infinite()
    
    def can_is_member_loop(self):
        return self.original_relation().can_is_member_loop()