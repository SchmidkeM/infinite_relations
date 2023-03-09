from src.relations.list_relation import ListRelation
from src.relations.relation_schema import RelationSchema
from src.relations.infinite_relations import AddRelation, NaturalNumbersRelation
from src.operations.union import Union
from src.operations.projection import Projection
from src.operations.selection import Selection
from src.operations.cross_join import CrossJoin
from src.operations.difference import Difference
from src.operations.derived.intersection import Intersection
from src.operations.derived.natural_join import NaturalJoin

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


# projekce
S2 = RelationSchema(["Age"])
P = Projection(R2, S2)


# restrikce
Sl = Selection(P, lambda Age: Age > 23)


# příklad nekonečné relace
Sa = RelationSchema(["x1", "x2", "suma"])
A = AddRelation(Sa)

Af = ListRelation(Sa)
x1 = [1, 2, 3, 4]
x2 = [3, 2, 1, 0]
sumy = [4, 4, 0, 4]
for i in range(len(x1)):
    Af.insert(Af.create_tuple([x1[i], x2[i], sumy[i]]))


# průnik
I = Intersection(A, Af)
I2 = Intersection(Af, A)

# kartézský součin
C = CrossJoin(Sl, A)

# rozdíl
R3 = ListRelation(S)
for i in range(len(names) - 1):
    R3.insert(R3.create_tuple([names[i], ages[i]]))
D = Difference(R2, R3)
Di = Difference(A, Af)

# přirozené spojení
R4 = ListRelation(RelationSchema(["Name", "x", "y"]))
xs = [1, 2, 3, 4]
ys = [2, 3, 1, 1]
for i in range(len(names)):
    R4.insert(R4.create_tuple([names[i], xs[i], ys[i]]))
N = NaturalJoin(R4, AddRelation())


# výsledky
print("Union")
U.print()
print("Projection")
P.print()
print("Selection")
Sl.print()
print("AddRelation")
A.print(10)
print("Intersection")
I.print()
I2.print()
print("Cartesian product")
C.print(10)
print("Difference")
D.print()
Di.print(20)
print("Natural join")
N.print(4)

# TODO:
# operace - rename?
# nekonečné relace
# testy?
# demonstrace
