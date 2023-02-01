import sys
from .relation import Relation

class AddRelation(Relation):
    def __init__(self):
        super().__init__([])
        self.iterator = self.__add_generator__()
        self.can_is_member_loop = False

    def __reset__(self):
        self.iterator = self.__add_generator__()

    def __add_generator__(self):
        for i in range(sys.maxsize):
            for j in range(i):
                yield [j, i-j, i]

    def is_member(self, element):
        return element[0] + element[1] == element[2]