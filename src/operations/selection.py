from __future__ import annotations
from ..relations.relation import Relation
from .unary_operation import UnaryOperation
from ..utils import get_parameter_names

class Selection(UnaryOperation):
    def __init__(self, relation: Relation, condition: function):
        super().__init__(relation)
        self.condition = condition
        self.condition_params = get_parameter_names(condition)
        
    def members(self):
        for tuple in self.original_relation().members():
            if self.condition(*[tuple[param] for param in self.condition_params]):
                yield tuple
    

