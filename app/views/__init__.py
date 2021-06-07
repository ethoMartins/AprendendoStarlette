from starlette.routing import Route, Mount

from .index import index
from .users import getUsers, setUser

routes = [
    Route("/",endpoint=index),
    Mount("/users", routes= [
          Route("/", endpoint=getUsers),
          Route("/", endpoint=setUser, methods=["POST"]),
        ]
    )
]