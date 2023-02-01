from Core.finite_relation import FiniteRelation
from Core.relation_schema import RelationSchema
from Core.union import Union

S = RelationSchema(["Name", "Age"])
R1 = FiniteRelation(S, [["Martin", 23], ["Anna", 24], ["Bert", 25]])
R2 = FiniteRelation(S, [["Dani", 23], ["Emil", 26], ["Franta", 25]])

U = Union(R1, R2)

U.print()


