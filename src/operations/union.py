from itertools import zip_longest
from ..relations.relation import Relation
from .binary_operation import BinaryOperation
from ..utils import flatten_list

class Union(BinaryOperation):

    def __init__(self, left: Relation, right: Relation):
        if not left.schema == right.schema:
            raise Exception("Cannot unite relations with different schemas")
        super().__init__(left.schema, left, right)

    def can_be_infinite(self):
        return self.left().can_be_infinite or self.right().can_be_infinite

    def can_is_member_loop(self):
        return self.left().can_is_member_loop or self.right().can_is_member_loop

    def is_member(self, element):
        if self.left().can_is_member_loop:
            return self.right().is_member(element) or self.left().is_member(element)
        else:
            return self.left().is_member(element) or self.right().is_member(element)
    
    def members(self):
        return iter(filter(lambda x: x != None, (flatten_list(zip_longest(self.left().members(), self.right().members())))))

        # members1 = self.left().members()
        # members2 = self.right().members()
        # depleted1 = False
        # depleted2 = False

        # while not (depleted1 and depleted2):
        #     if not depleted1:
        #         try:
        #             yield next(members1)
        #         except StopIteration:
        #             depleted1 = True
        #     if not depleted2:
        #         try:
        #             yield next(members2)
        #         except StopIteration:
        #             depleted2 = True
