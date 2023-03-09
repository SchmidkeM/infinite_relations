from __future__ import annotations
from ..utils import compare_lists_orderless

class RelationSchema:
    def __init__(self, attribute_list: list):
        self.attribute_list: list = attribute_list

    def cross_with(self, S2: RelationSchema):
        new_schema: RelationSchema = RelationSchema(self.attribute_list.copy())
        for attr in S2.attribute_list:
            if attr in new_schema.attribute_list:
                new_schema.attribute_list.append(attr + "_")
            else:
                new_schema.attribute_list.append(attr)
        return new_schema

    def join_with(self, S2: RelationSchema):
        new_schema = RelationSchema(self.attribute_list.copy())
        common_attrs_list: list = []
        for attr in S2.attribute_list:
            if attr in new_schema.attribute_list:
                common_attrs_list.append(attr)
            else:
                new_schema.attribute_list.append(attr)
        return (new_schema, common_attrs_list)
    
    def __len__(self):
        return len(self.attribute_list)

    def __eq__(self, object):
        return isinstance(object, RelationSchema) and compare_lists_orderless(object.attribute_list, self.attribute_list)

    def print(self):
        for attr in self.attribute_list:
            print(attr, end=" ")
        print("")

    def __create_tuple__(self, values: list):
        if len(values) == len(self):
            return dict(zip(self.attribute_list, values))
        else:
            raise Exception("Wrong number of values to create a tuple")
        
    def is_subset_of(self, schema: RelationSchema):
        return all(item in schema.attribute_list for item in self.attribute_list)
