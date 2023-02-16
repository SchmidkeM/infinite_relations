from src.relations.list_relation import ListRelation
from src.relations.relation_schema import RelationSchema
from src.relations.infinite_relations import AddRelation
from src.operations.union import Union
from src.operations.projection import Projection
from src.operations.selection import Selection

S = RelationSchema(["Name", "Age"])

R1 = ListRelation(S, [{ "name": "Martin", "age": 23 }, { "name": "Anna", "age": 24 }])

names = ["Dani", "Emil", "Franta"]
ages = [23, 26, 25]
R2 = ListRelation(S)
for i in range(len(names)):
    R2.insert(R2.create_tuple([names[i], ages[i]]))

U = Union(R1, R2)
U.print()

S2 = RelationSchema(["Age"])
P = Projection(R2, S2)
P.print()

Sl = Selection(P, lambda Age: Age > 23)
Sl.print()


A = AddRelation()
A.print(10)


# union: set
# dopsat všechny operace
# příklady nekonečných relací
# testy
# hodně demonstrací
