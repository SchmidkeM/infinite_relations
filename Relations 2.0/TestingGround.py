from Src.Relations.finite_relation import FiniteRelation
from Src.Relations.relation_schema import RelationSchema
from Src.Relations.infinite_relations import AddRelation
from Src.Operations.union import Union

S = RelationSchema(["Name", "Age"])
R1 = FiniteRelation(S, [["Martin", 23], ["Anna", 24]])
R2 = FiniteRelation(S, [["Dani", 23], ["Emil", 26], ["Franta", 25]])

U = Union(R1, R2)

U.print()


AddRelation().print()


# reprezentovat n-tice jako slovníky
# typová kontrola skrz Keys slovníku
# funkce pro zakládání n-tic podle schématu
# dopsat všechny operace
# příklady nekonečných relací
# testy
# hodně demonstrací
