from starlette.applications import Starlette

from .views import routes
from .model import sqlalchemy#, dbase



def create_app():
    
    app = Starlette(
        debug=True,
        routes=routes,
        # on_startup=[dbase.connect],
        # on_shutdown=[dbase.disconnect]
        )
    
    return app