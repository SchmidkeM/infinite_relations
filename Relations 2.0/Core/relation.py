from __future__ import annotations
import sys


class RelationSchema:
    def __init__(self, attribute_list: list):
        self.attribute_list: list = attribute_list

    def get_attribute_indices(self, selected_attributes: list | RelationSchema ):
        indices_list: list = []
        selected_attributes_list = selected_attributes if selected_attributes is list else selected_attributes.attribute_list
        for attr in selected_attributes_list:
            if attr in self.attributes_list:
                indices_list += [self.attribute_list.index(attr)]
    
    def add_attr(self, attr_name):
        self.attribute_list += [attr_name]

    def cross_with(self, S2: RelationSchema):
        new_schema: RelationSchema = RelationSchema(self.attribute_list.copy())
        for attr in S2.attribute_list:
            if attr in new_schema.attribute_list:
                new_schema.add_attr(attr + "#2")
            else:
                new_schema.add_attr(attr)
        return new_schema

    def join_with(self, S2: RelationSchema):
        new_schema = RelationSchema(self.attribute_list.copy())
        common_attrs_list: list = []
        for attr in S2.attribute_list:
            if attr in new_schema.attribute_list:
                common_attrs_list += [attr]
            else:
                new_schema.add_attr(attr)
        return (new_schema, common_attrs_list)


# class Tuple:
#     def __init__(self, attrs: list):
#         self.attr_list = attrs

#     def project(self, schema: RelationSchema):

#     def cross_with(self, tuple: Tuple):

#     def get_attr(self, attr_name: string): # najit jak overridnout [] operator

#     def get_attr_index(self, attr_name: string): # možná nebude třeba


# class GeneratorFactory:
    # def __init__(self)
        # pass

    # def create_generator_function(self, vzorcem zadaná číselná řada)
      


# základní obecná relace
# Potomci budou pravděpodobně jen konkrétní relace z api, konečná a nekonečná relace se odlišují atributy "can_..."
class Relation:

    def __init__(self, schema: RelationSchema, tuples=[]):
        self.schema: RelationSchema = schema
        self.initial_state: list  = tuples
        self.generator = (x for x in tuples)
        self.can_be_infinite: bool = True
        self.can_is_member_loop: bool = True

    def is_list_based(self):
        return self.initial_state is list

    def try_get_next_tuple(self):
        try:
            return next(self.generator)
        except StopIteration:
            return None

    def __reset__(self):
        if self.is_list_based():
            self.generator = (x for x in self.initial_state)
        else:
            self.generator = self.initial_state()

    def members(self, limit=sys.maxsize):
        if self.can_be_infinite:
            Warning("Trying to get members of infinite relation, loop possible")
        member_list = []
        for _ in range(limit):
            try:
                member_list.append(next(self.generator))
            except StopIteration:
                self.__reset__()
                return member_list
        self.__reset__()
        return member_list

    def is_member(self, element):
        if self.can_is_member_loop:
            Warning("Infinite loop possible!")
        while True:
            try:
                member_element = next(self.generator)
                if member_element == element:
                    self.__reset__()
                    return True
            except StopIteration:
                self.__reset__()
                return False

    def print(self, limit=100):
        for tuple in self.members(limit):
            print(tuple)

    def insert(self, tuple: list):
        if not self.can_be_infinite:
            if not len(tuple) == len(self.schema):
                Exception("trying to insert incorrect length tuple")
            self.initial_state += [tuple]
        else:
            Exception("Insert to infinite relations not supported")


def unite(r: Relation, r2: Relation):
    if not r.schema == r2.schema:
        Exception("Cannot unite relations over different schemas")
    if not r.can_be_infinite and not r2.can_be_infinite:
        return Relation(r.members() + r2.members())
    else:
        pass 
    # intertwine_generators(r.)

def intersect(r: Relation, r2: Relation):
    if not r.schema == r2.schema:
        Exception("Cannot intersect relations over different schemas")
    if not r.can_be_infinite:
        return Relation([x for x in r.members() if r2.is_member(x)])
    else:
        pass

def project(r: Relation, new_schema: RelationSchema):
    result: Relation = Relation(new_schema)
    if not r.can_be_infinite:
        for tuple in r.tuples:
            projected_tuple = []
            projection_indices = r.schema.get_attribute_indices(new_schema)
            for index in projection_indices:
                projected_tuple += [tuple[index]] 
            result.insert(projected_tuple)
        return result
    else:
        pass


def select(r: Relation, condition: function, attr_names_list: list):
    if not r.can_be_infinite:
        for tuple in r.members():
            values_list: list = []
            for attr_name in attr_names_list:
                values_list.append(tuple[attr_name])
        return Relation(r.schema, [x for x in r.members() if condition(values_list)])#x[*attr_names_list])])
    else:
        pass

def cross(r: Relation, r2: Relation):
    cross_schema: RelationSchema = r.schema.cross_with(r2.schema)
    if not r.can_be_infinite and not r2.can_be_infinite:
        result = Relation(cross_schema)
        for tuple in r.members():
            for tuple2 in r2.members():
                result.insert(tuple + tuple2)
        return result
    else:
        pass

def join(r: Relation, r2: Relation):
    join_schema_result = r.schema.join_with(r2.schema)
    join_schema: RelationSchema = join_schema_result[0]
    common_attrs: list = join_schema_result[1]
    
    result = cross(r, r2)
    for common_attr_name, common_attr_name2 in zip(common_attrs, [attr+"#2" for attr in common_attrs]):
        result = select(result, lambda x,y: x==y, [common_attr_name, common_attr_name2])
    return result.project(join_schema)



# příklad relace z api
class AddRelation(Relation):
    def __init__(self):
        super().__init__([])
        self.generator = self.__add_generator__()
        self.can_is_member_loop = False

    def __reset__(self):
        self.generator = self.__add_generator__()

    def __add_generator__(self):
        for i in range(sys.maxsize):
            for j in range(i):
                yield [j, i-j, i]

    def is_member(self, element):
        return element[0] + element[1] == element[2]


# test
r1 = Relation([1, 2, 3])
r2 = Relation(['a', 'b', 'c', 'd'])

print("--union--")
unite(r1, r2).print()

print("--intersection--")
intersect(r1, r2).print()

print("--selection--")
select(r1, lambda x: x>1).print()

print("--add relation--")
AddRelation().print()