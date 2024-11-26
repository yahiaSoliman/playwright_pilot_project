import time

import pytest
from backend_automation.endpoints import EndPoints
from testData import TestData
from backend_automation.Object import Object


class TestRelations:
    relation_type_id = 10

    @pytest.fixture
    def user_token(self):
        login_response = EndPoints.login(TestData.url_staging_qa_api, TestData.staging_qa_user_01)
        token = login_response.json()['data']['token']
        return token

    def test_subitem_relation_between_two_items(self, user_token):
        ob_1 = Object(user_token, TestData.url_staging_qa_api)  # create class object
        name = "automation_item_" + TestData.generate_random_name(4)  # generate random name
        response = ob_1.create(name, 27, 1, 1, 4)  # create new object
        assert 201 == response.status_code

        ob_2 = Object(user_token, TestData.url_staging_qa_api)  # create class object
        name = "automation_item_" + TestData.generate_random_name(4)  # generate random name
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