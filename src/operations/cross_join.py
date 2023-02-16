from .binary_operation import BinaryOperation
from ..relations.relation import Relation
from ..utils import dict_from_lists

class CrossJoin(BinaryOperation):
    def __init__(self, left: Relation, right: Relation):
        super().__init__(left.schema().cross_with(right.schema()), left, right)
        self.__left__ = left
        self.__right__ = right

    def can_be_infinite(self):
        return self.left().can_be_infinite() or self.right().can_be_infinite()

    def can_is_member_loop(self):
        return self.left().can_is_member_loop() or self.right().can_is_member_loop()
    
    def members(self):
        if self.left().can_be_infinite():
            for leftuple in self.left().members():
                for rightuple in self.right().members():
                    yield dict_from_lists(self.schema().attribute_list, list(leftuple.values()) + list(rightuple.values()))
        else:
            for rightuple in self.right().members():
                for leftuple in self.left().members():
                    yield dict_from_lists(self.schema().attribute_list, list(leftuple.values()) + list(rightuple.values()))