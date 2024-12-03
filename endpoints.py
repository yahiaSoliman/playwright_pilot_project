import json

import requests


class EndPoints:

    @staticmethod
    def login(url, credentials):
        login_payload = json.dumps({

            "tenant_password": credentials['password'],
            "tenant_username": credentials['email']
        })
        login_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        login_url = url + "login/"
        login_response = requests.request("POST", login_url, headers=login_headers, data=login_payload)

        assert login_response.status_code == 200, print(login_response.text)
        # print("user is logged in successfully")
        return login_response

    @staticmethod
    def get_layout(user_token, url):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'authorization': 'token ' + user_token
        }

        url = url + "api/users/manage_user_layout/"
        layout_response = requests.request("GET", url, headers=headers, data=json.dumps({}))
        assert layout_response.status_code == 200, print(layout_response.text)
        # print("user dashboards and tabs are received successfully")
        return layout_response.json()

    @staticmethod
    def close_all_tabs(user_token, app_id, dashboard_id, url):
        query_parameters = {
            "app_id": app_id,
            "dashboard_id": dashboard_id,
            "delete_flag": "close_all"
        }
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'authorization': 'token ' + user_token
        }

        url = url + "api/users/manage_user_layout/"
        layout_response = requests.request("DELETE", url, headers=headers, params=query_parameters)
        assert layout_response.status_code == 200
        # print("all tabs of active dashboard are closed successfully")
        return layout_response.json()

    @staticmethod
    def create_object(user_token, object_name, object_type_id, owner_id, workspace_id, url, lifecycle):
        payload = json.dumps({
            "workspace": workspace_id,
            "lifecycle": lifecycle,
            "owner": owner_id,
            "name": object_name,
            "type": object_type_id})

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'authorization': 'token ' + user_token
        }

        url = url + "api/system/object/"
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    @staticmethod
    def modify_object(user_token, object_id, url, changes_dict):
        changes_dict.update({"object_id": object_id})
        payload = json.dumps([
            changes_dict
        ])

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'authorization': 'token ' + user_token
        }

        url = url + "api/system/objects/bulk_update/"
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    @staticmethod
    def delete_object(user_token, object_id, url):
        payload = json.dumps({"object_ids": [
            object_id
        ]
        })

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'authorization': 'token ' + user_token
        }

        url = url + "api/system/bulk_objects/delete/"
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    @staticmethod
    def revise_object(user_token, object_id, url):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'authorization': 'token ' + user_token
        }

        url = url + f"api/system/objects/revise/{object_id}/"
        response = requests.request("GET", url, headers=headers)
        return response

    @staticmethod
    def iterate_object(user_token, object_id, url):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'authorization': 'token ' + user_token
        }

        url = url + f"api/system/objects/iterate/{object_id}/"
        response = requests.request("GET", url, headers=headers)
        return response

    @staticmethod
    def promote_object(user_token, object_id, url):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'authorization': 'token ' + user_token
        }

        url = url + f"api/system/objects/promote/{object_id}/"
        response = requests.request("GET", url, headers=headers)
        return response

    @staticmethod
    def demote_object(user_token, object_id, url):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'authorization': 'token ' + user_token
        }

        url = url + f"api/system/objects/demote/{object_id}/"
        response = requests.request("GET", url, headers=headers)
        return response

    @staticmethod
    def get_object_types(user_token, url):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'authorization': 'token ' + user_token
        }

        url = url + f"api/system/type/?is_system=false"
        response = requests.request("GET", url, headers=headers)
        return response

    @staticmethod
    def change_object_ownership(user_token, url, command_id, object_id):
        payload = json.dumps({
            "object_id": [
                object_id
            ]
        })

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'authorization': 'token ' + user_token
        }
        url = url + f"api/system/command/execute/{command_id}/"
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    @staticmethod
    def get_object_details(user_token, url, object_id):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'authorization': 'token ' + user_token
        }
        url = url + f"api/system/object/{object_id}/"
        response = requests.request("GET", url, headers=headers)
        return response

    @staticmethod
    def reserve_object(token, url, object_id, object_type, context_type):
        payload = json.dumps({
            "object_id": [
                object_id
            ],
            "type": object_type,
            "context_type": context_type
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'authorization': 'token ' + token
        }
        url = url + "api/system/command/execute/191/"
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    @staticmethod
    def unreserve_object(token, url, object_id, object_type, context_type):
        payload = json.dumps({
            "object_id": [
                object_id
            ],
            "type": object_type,
            "context_type": context_type
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'authorization': 'token ' + token
        }
        url = url + "api/system/command/execute/192/"
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    @staticmethod
    def export_object(token, url, object_type):
        payload = json.dumps(
            {
                "type": object_type,
                "context_type": 1
            }
        )
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'authorization': 'token ' + token
        }
        url = url + "api/system/command/execute/178/"
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    @staticmethod
    def create_relation(token, url, from_object_id, to_object_id, relation_type_id):
        payload = json.dumps({
            "relation_list": [
                {
                    "from_id": from_object_id,
                    "to_id": to_object_id,
                    "relationship": relation_type_id
                }
            ],
            "bulk_relation": False
        })

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'authorization': 'token ' + token
        }
        url = url + "/api/system/relations/new_bulk_update/"
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    @staticmethod
    def delete_relation(token, url, relation_id):
        payload = json.dumps({
            "relation_ids": [{"relation_id": relation_id}]
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'authorization': 'token ' + token
        }
        url = url + "/api/system/relations/bulk_relation_delete/"
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    @staticmethod
    def get_related_objects(token, url, object_id, direction):
        Qparams = {
            "direction": str(direction)
        }
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'authorization': 'token ' + token
        }
        url = url + f"api/system/objects/related/{object_id}/"
        response = requests.request("GET", url, headers=headers, params=Qparams)
        return response

    @staticmethod
    def get_allowed_relationships_between_two_object_types(token, url, object_type_from, object_type_to):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'authorization': 'token ' + token
        }
        url = url + f"api/system/type/relationships/from/{object_type_from}/to/{object_type_to}/"
        response = requests.request("GET", url, headers=headers)
        return response
