import graphene
import json

class Userss(graphene.ObjectType):
    user_id = graphene.ID()
    user_name = graphene.String()
    password = graphene.String()
    email = graphene.String()
    profile_picture = graphene.String()
    role = graphene.String()

class Query(graphene.ObjectType):
    users = graphene.List(Userss)

    def resolve_users(self, info):
        # with open("users.json", "r") as in_file:
        #     users_data = json.load(in_file)
        users_data = [{"user_id": "aa1234", "user_name": "aatest", "password": "password", "email": "aa1234@columbia.edu", "profile_picture": "1", "role": "Student"}, {"user_id": "bb1234", "user_name": "bbtest", "password": "password", "email": "bb1234@columbia.edu", "profile_picture": "1", "role": "Admin"}, {"user_id": "cc1234", "user_name": "cctest", "password": "password", "email": "cc1234@columbia.edu", "profile_picture": "1", "role": "Student"}, {"user_id": "dd1234", "user_name": "ddtest", "password": "password", "email": "dd1234@columbia.edu", "profile_picture": "1", "role": "Student"}, {"user_id": "ee1234", "user_name": "eetest", "password": "password", "email": "ee1234@columbia.edu", "profile_picture": "1", "role": "IT Faculty"}, {"user_id": "ff1234", "user_name": "fftest", "password": "password", "email": "ff1234@columbia.edu", "profile_picture": "1", "role": "Student"}]
        users = [Userss(**user) for user in users_data]
        # return Userss(user_id= "aa1234", user_name= "aatest", password= "password", email= "aa1234@columbia.edu", profile_picture= "1", role= "Student")
        return users

schema = graphene.Schema(query=Query)

# query_string = '{ users { userId, userName, password, email, profilePicture, role } }'
# result = schema.execute(query_string)

# print(result)
