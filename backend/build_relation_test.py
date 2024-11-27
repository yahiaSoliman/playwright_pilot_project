import pytest

from Object import Object
from endpoints import EndPoints
from data import data


class TestRelations:
    relation_type_id = 10

    @pytest.fixture
    def user_token(self):
        login_response = EndPoints.login(data.url_staging_qa_api, data.staging_qa_user_01)
        token = login_response.json()['data']['token']
        return token

    def test_subitem_relation_between_two_items(self, user_token):
        ob_1 = Object(user_token, data.url_staging_qa_api)  # create class object
        name = "automation_item_" + data.generate_random_name(4)  # generate random name
        response = ob_1.create(name, 27, 1, 1, 4)  # create new object
        assert 201 == response.status_code

        ob_2 = Object(user_token, data.url_staging_qa_api)  # create class object
        name = "automation_item_" + data.generate_random_name(4)  # generate random name
        response = ob_2.create(name, 27, 1, 1, 4)  # create new object
        assert 201 == response.status_code

        response = ob_1.create_relation(ob_2.id, self.relation_type_id)
        assert 201 == response.status_code

        response = ob_1.get_related_objects("TO")
        assert 200 == response.status_code

        assert 1 == len(response.json()['to'])
        assert ob_2.id == response.json()['to'][0]['object_id']

        response = ob_2.get_related_objects("FROM")
        assert 200 == response.status_code

        assert 1 == len(response.json()['from'])
        assert ob_1.id == response.json()['from'][0]['object_id']
