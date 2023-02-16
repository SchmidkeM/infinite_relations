from src.relations.list_relation import ListRelation
from src.relations.relation_schema import RelationSchema
from src.relations.infinite_relations import AddRelation
from src.operations.union import Union
from src.operations.projection import Projection
from src.operations.selection import Selection
from src.operations.intersection import Intersection
from src.operations.cross_join import CrossJoin

# iniciace

# vytvoření schématu
S = RelationSchema(["Name", "Age"])

# vytvoření relace rovnou se seznamem slovníků
R1 = ListRelation(S, [{ "Name": "Martin", "Age": 23 }, { "Name": "Anna", "Age": 24 }])

# vytvoření relace a přidání slovníků ze seznamů hodnot
names = ["Dani", "Emil", "Franta", "Martin"]
ages = [23, 26, 25, 23]
R2 = ListRelation(S)
for i in range(len(names)):
    R2.insert(R2.create_tuple([names[i], ages[i]]))


# sjednocení
U = Union(R1, R2)
U.print()


# projekce
S2 = RelationSchema(["Age"])
P = Projection(R2, S2)
P.print()


# restrikce
Sl = Selection(P, lambda Age: Age > 23)
Sl.print()


# příklad nekonečné relace
Sa = RelationSchema(["x1", "x2", "suma"])
A = AddRelation(Sa)
A.print(10)


Af = ListRelation(Sa)
x1 = [1, 2, 3, 4]
x2 = [3, 2, 1, 0]
sumy = [4, 4, 0, 4]
for i in range(len(x1)):
    Af.insert(Af.create_tuple([x1[i], x2[i], sumy[i]]))


# průnik
I = Intersection(A, Af)
#I.print()

I2 = Intersection(Af, A)
#I2.print()


# kartézský součin
C = CrossJoin(Sl, A)
C.print(10)

# operace - todo: test Subtraction, natural_join, intersection skrz subtraction
# nekonečné relace
# testy
# demonstrace
