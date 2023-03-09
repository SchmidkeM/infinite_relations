from ..binary_operation import BinaryOperation
from ..cross_join import CrossJoin
from ..projection import Projection
from ..selection import Selection
from ...relations.relation import Relation

class NaturalJoin(BinaryOperation):
    def __init__(self, left: Relation, right: Relation):
        join_schema, common = left.schema().join_with(right.schema())
        super().__init__(join_schema, left, right)
        self.__left__ = left
        self.__right__ = right
        self.__common__ = common

    def can_be_infinite(self):
        return self.left().can_be_infinite() or self.right().can_be_infinite()

    def can_is_member_loop(self):
        return self.left().can_is_member_loop() or self.right().can_is_member_loop()
    
    def members(self):
        result = CrossJoin(self.left(), self.right())

        common_attrs_eq_conds = []
        for a_name, a_name2 in zip(self.__common__, map(lambda x: x+"_", self.__common__)):
            common_attrs_eq_conds.append("lambda {attr}, {attr2}: {attr} == {attr2}".format(attr=a_name, attr2=a_name2))
        for cond in common_attrs_eq_conds:
            result = Selection(result, eval(cond))

        return Projection(result, self.schema()).members()
