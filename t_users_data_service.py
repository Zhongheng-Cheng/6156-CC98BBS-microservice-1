import json
from resources.users.users_data_service import UserDataService


def get_data_service():

    config = {
        "data_directory": "data",
        "data_file": "users.json"
    }

    ds = UserDataService(config)
    return ds


def t1():

    ds = get_data_service()
    users = ds.get_users(role="Student")
    print("t1: users = ", json.dumps(users, indent=2))

    
    print("=================")
    # creating new user
    # ds.create_user(
    #     user_id= "gg1234",
    #     user_name= "ggtest",
    #     password= "password",
    #     email= "gg1234@columbia.edu",
    # )
    # ds.update_user(user_id="ff1234", password="ffpassword")
    ds.delete_user(user_id='gg1234')

    print('===================')
    ds = get_data_service()
    users = ds.get_users(role="Student")
    print("t1: users = ", json.dumps(users, indent=2))

if __name__ == "__main__":
    t1()

    