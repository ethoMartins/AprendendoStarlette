from starlette.responses import PlainTextResponse


def index( response ):
    return PlainTextResponse("Salve!")