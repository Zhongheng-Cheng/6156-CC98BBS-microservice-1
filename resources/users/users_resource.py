from resources.abstract_base_resource import BaseResource
from resources.users.user_models import UserRspModel, UserModel
from resources.rest_models import Link
from typing import List


class UsersResource(BaseResource):
    #
    # This code is just to get us started.
    # It is also pretty sloppy code.
    #

    def __init__(self, config: dict):
        super().__init__()

        self.data_service = config["data_service"]

    @staticmethod
    def _generate_links(s: dict) -> UserRspModel:

        self_link = Link(**{
            "rel": "self",
            "href": "/users/" + s['user_id']
        })

        links = [
            self_link
        ]
        rsp = UserRspModel(**s, links=links)
        return rsp

    def get_users(self,
                  user_id: str = None, 
                  user_name: str = None, 
                  password: str = None,
                  email: str = None,
                  profile_picture: str = None,
                  role: str = None
                  ) -> List[UserRspModel]:

        result = self.data_service.get_users(user_id, user_name, password, email, profile_picture, role)
        final_result = []

        for s in result:
            m = self._generate_links(s)
            final_result.append(m)

        return final_result
    
    def create_user(self,
                  user_id: str = None, 
                  user_name: str = None, 
                  password: str = None,
                  email: str = None,
                  profile_picture: str = None,
                  role: str = None
                  ):
        result = self.data_service.create_user(user_id, user_name, password, email, profile_picture, role)
        return result