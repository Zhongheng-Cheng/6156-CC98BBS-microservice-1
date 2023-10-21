from resources.users.users_resource import UsersResource
from resources.users.users_data_service import UserDataService
import json


def get_data_service():

    config = {
        "data_directory": "data",
        "data_file": "users.json"
    }

    ds = UserDataService(config)
    return ds


def get_user_resource():
    ds = get_data_service()
    config = {
        "data_service": ds
    }
    res = UsersResource(config)
    return res


def t1():

    s = get_user_resource()
    res = s.get_users(role="Student")
    print("t1: res = ", json.dumps(res, indent=2, default=str))


if __name__ == "__main__":
    t1()