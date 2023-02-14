from __future__ import annotations

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
    
    def __len__(self):
        return len(self.attribute_list)

    def print(self):
        for attr in self.attribute_list:
            print(attr, end=" ")
        print("")