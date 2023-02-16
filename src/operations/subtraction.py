from ..relations.relation import Relation
from .binary_operation import BinaryOperation

class Subtraction(BinaryOperation):

    def __init__(self, left: Relation, right: Relation):
        if not left.schema() == right.schema():
            raise Exception("Cannot subtract relations with different schemas")
        super().__init__(left.schema(), left, right)

    def can_be_infinite(self):
        return self.left().can_be_infinite()

    def can_is_member_loop(self):
        return self.left().can_is_member_loop() or self.right().can_is_member_loop()

    def is_member(self, element):
        return self.left().is_member(element) and not self.right().is_member(element)
    
    def members(self):
        return (tuple for tuple in self.left().members() if tuple not in self.right().members())