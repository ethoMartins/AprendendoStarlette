from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import PlainTextResponse


def index(request):
    return PlainTextResponse("Salve!")

def login(request):
    return PlainTextResponse(str(dir(request)))

routes = [
    Route("/", endpoint=index),
    Route("/login", endpoint=login),
]

app = Starlette(debug=True, routes=routes)