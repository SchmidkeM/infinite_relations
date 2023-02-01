from ..BaseRelations.relation import Relation

class Union(Relation):

    def __init__(self, r1: Relation, r2: Relation):
        if not r1.schema == r2.schema:
            Exception("Cannot unite relations with different schemas")
        super(Union, self).__init__(r1.schema)
        self.r1: Relation = r1
        self.r2: Relation = r2

    def can_be_infinite(self):
        return self.r1.can_be_infinite or self.r2.can_be_infinite

    def can_is_member_loop(self):
        return self.r1.can_is_member_loop or self.r2.can_is_member_loop

    def is_member(self, element):
        return self.r1.is_member(element) or self.r2.is_member(element)
    
    def members(self):
        members1 = self.r1.members()
        members2 = self.r2.members()
        depleted1 = False
        depleted2 = False

        while not (depleted1 and depleted2):
            if not depleted1:
                try:
                    yield next(members1)
                except StopIteration:
                    depleted1 = True
            if not depleted2:
                try:
                    yield next(members2)
                except StopIteration:
                    depleted2 = True

    def print(self):
        super(Union, self).print()

        members = self.members()
        while True:
            try:
                print(next(members))
            except StopIteration:
                return

