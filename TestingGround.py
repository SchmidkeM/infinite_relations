from src.relations.list_relation import ListRelation
from src.relations.relation_schema import RelationSchema
from src.relations.infinite_relations import AddRelation
from src.operations.union import Union

S = RelationSchema(["Name", "Age"])
R1 = ListRelation(S, [["Martin", 23], ["Anna", 24]])
R2 = ListRelation(S, [["Dani", 23], ["Emil", 26], ["Franta", 25]])

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
