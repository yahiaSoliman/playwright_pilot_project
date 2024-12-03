import random
import re
import string



"""
url = "https://oldtest.bumblebeeeee.com/login"
username = "tester"
password = "Raqz3Ts0D2fN"

https://development.bumblebeeeee.com/
User: tester
Password: Raqz3Ts0D2fN

https://qa.staging.bumblebeeeee.com/
User: qa.cerebital
Password: OY0n/dn,K3uJ3k+
"""


class Data:
    change_owner_command_id_qa_stg = 194
    change_owner_command_id_yahiadev_dev = 61
    url_staging_qa_api = "https://qa.api.staging.bumblebeeeee.com/"
    url_staging_qa_ui = "https://qa.staging.bumblebeeeee.com/"
    url_development_yahiadev_api = "https://yahiadev.api.bumblebeeeee.com/"
    development_yahiadev_user_01 = {
        "email": "yahia_development_tenant_01@mailslurp.net",
        "password": "P@ssw0rd"
    }
    staging_qa_user_01 = {
        "email": "qa.cerebital",
        "password": "OY0n/dn,K3uJ3k+"
    }
    username = "qa.cerebital"
    password = "OY0n/dn,K3uJ3k+"
    new_account_password = "P@ssw0rd"
    new_account_first_name = "yahia"
    new_account_last_name = "soliman"
    search_query = "test"
    type_filter_value = "item"

    # new email to be used in registration

    # otp to be used in registration
    @staticmethod
    def get_otp_from_email_content(email_content):
        return re.search('<p>OTP: <b>([0-9]{6})</b></p>', email_content).group(1)

    # domain name to be used in registration
    @staticmethod
    def generate_random_name(string_length):
        return ''.join(random.choices(string.ascii_lowercase, k=string_length))
