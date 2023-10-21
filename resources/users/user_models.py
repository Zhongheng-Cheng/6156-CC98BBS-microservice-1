from __future__ import annotations
from pydantic import BaseModel
from typing import List

from resources.rest_models import Link


class UserModel(BaseModel):
    user_id: str
    user_name: str
    password: str
    email: str
    profile_picture: str
    role: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "user_id": "zc2737",
                    "user_name": "Zhongheng Cheng",
                    "password": "password",
                    "email": "zc2737@columbia.edu",
                    "profile_picture": "",
                    "role": "Ordinary user"
                }
            ]
        }
    }


class UserRspModel(UserModel):
    links: List[Link] = None