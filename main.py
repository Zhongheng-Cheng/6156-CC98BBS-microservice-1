#
# FastAPI is a framework and library for implementing REST web services in Python.
# https://fastapi.tiangolo.com/
#
from fastapi import FastAPI, Response, HTTPException, Request
from fastapi.responses import RedirectResponse

from fastapi.staticfiles import StaticFiles
from typing import List, Union
import time
import sys

import uvicorn

from resources.users.users_resource import UsersResource
from resources.users.users_data_service import UserDataService
from resources.users.user_models import UserModel, UserRspModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

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


users_resource = get_user_resource()


# Middleware function: record processing time and contain it in the response header
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/")
async def root():
    return RedirectResponse("/static/index.html")


@app.get("/users-graphql")
async def get_users_graphql(query: str):
    from data.graphql_test import schema
    print(query)
    res = schema.execute(query)
    print(res)
    return res.data


@app.get("/users", response_model=List[UserRspModel])
async def get_users(user_id: str = None, 
                    user_name: str = None, 
                    password: str = None,
                    email: str = None,
                    profile_picture: str = None,
                    role: str = None):
    """
    Return a list of users matching a query string.

    - **user_id**: user's id
    - **user_name**: user's name
    - **password**: user's password
    - **email**: user's email
    - **profile_picture**: user's profile_picture
    - **role**: user's role, ["Student", "Admin", "IT Faculty"]
    """
    result = users_resource.get_users(user_id, user_name, password, email, profile_picture, role)
    return result


@app.post("/users")
async def post_users(user_id: str = None, 
                    user_name: str = None, 
                    password: str = None,
                    email: str = None,
                    profile_picture: str = None,
                    role: str = None
                    ):
    users_resource.create_user(user_id, user_name, password, email, profile_picture, role)
    return 


@app.put('/users')
async def put_users(user_id: str = None, 
                    user_name: str = None, 
                    password: str = None,
                    email: str = None,
                    profile_picture: str = None,
                    role: str = None
                    ):
    kwargs = {key: value for key, value in locals().items() if value is not None}
    users_resource.update_user(**kwargs)
    return

@app.delete('/users')
async def delete_user(user_id: str = None, 
                    user_name: str = None, 
                    password: str = None,
                    email: str = None,
                    profile_picture: str = None,
                    role: str = None
                    ):
    kwargs = {key: value for key, value in locals().items() if value is not None}
    users_resource.delete_user(**kwargs)
    return


@app.get("/users/{user_id}", response_model=Union[UserRspModel, None])
async def get_user(user_id: str):
    """
    Return a user based on user_id.

    - **user_id**: user's id
    """
    result = None
    result = users_resource.get_users(user_id)
    if len(result) == 1:
        result = result[0]
    else:
        raise HTTPException(status_code=404, detail="Not found")
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(sys.argv[1]))
