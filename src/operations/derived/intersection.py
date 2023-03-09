from itertools import zip_longest
from ...relations.relation import Relation
from ..binary_operation import BinaryOperation
from ..difference import Difference


class Intersection(BinaryOperation):

    def __init__(self, left: Relation, right: Relation):
        if not left.schema() == right.schema():
            raise Exception("Cannot intersect relations with different schemas")
        super().__init__(left.schema(), left, right)

    def can_be_infinite(self):
        return self.left().can_be_infinite() and self.right().can_be_infinite()

    def can_is_member_loop(self):
        return self.left().can_is_member_loop() and self.right().can_is_member_loop()

    def is_member(self, element):
        if self.left().can_is_member_loop():
            return self.right().is_member(element) and self.left().is_member(element)
        else:
            return self.left().is_member(element) and self.right().is_member(element)
    
    def members(self):
        if self.left().can_be_infinite():
            return Difference(self.right(), Difference(self.right(), self.left())).members()
        else:
            return Difference(self.left(), Difference(self.left(), self.right())).members()
