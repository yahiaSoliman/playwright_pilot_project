from endpoints import EndPoints


class Object:

    def __init__(self, token, url):
        self.id = None
        self.token = token
        self.url = url

    def __str__(self):
        return 'object id is {}'.format(self.id)

    def create(self, object_name, object_type_id, owner_id, workspace_id, lifecycle):
        response_json = EndPoints.create_object(self.token, object_name, object_type_id, owner_id, workspace_id,
                                                self.url, lifecycle)
        self.id = response_json.json()['object_id']
        return response_json

    def modify(self, changes_dict):
        response_json = EndPoints.modify_object(self.token, self.id, self.url, changes_dict)
        return response_json

    def revise(self):
        response_json = EndPoints.revise_object(self.token, self.id, self.url)
        return response_json

    def iterate(self):
        response_json = EndPoints.iterate_object(self.token, self.id, self.url)
        return response_json

    def promote(self):
        response_json = EndPoints.promote_object(self.token, self.id, self.url)
        return response_json

    def demote(self):
        response_json = EndPoints.demote_object(self.token, self.id, self.url)
        return response_json

    def delete(self):
        response_json = EndPoints.delete_object(self.token, self.id, self.url)
        return response_json

    def change_ownership(self, command_id):
        response_json = EndPoints.change_object_ownership(self.token, self.url, command_id, self.id)
        return response_json

    def get_details(self):
        response_json = EndPoints.get_object_details(self.token, self.url, self.id)
        return response_json

    def reserve(self, object_type_id, context_id):
        response_json = EndPoints.reserve_object(self.token, self.url, self.id, object_type_id, context_id)
        return response_json

    def unreserve(self, object_type_id, context_id):
        response_json = EndPoints.unreserve_object(self.token, self.url, self.id, object_type_id, context_id)
        return response_json

    def export(self, object_type_id):
        response_json = EndPoints.export_object(self.token, self.url, object_type_id)
        return response_json

    def create_relation(self, to_object_id, relation_type_id):
        response = EndPoints.create_relation(self.token, self.url, self.id, to_object_id, relation_type_id)
        return response

    def get_related_objects(self, direction):
        response = EndPoints.get_related_objects(self.token, self.url, self.id, direction)
        return response




