from sqlalchemy.orm import session
from starlette.responses import JSONResponse
from starlette.requests import Request
from app.model import User, Session


session = Session()

async def getUsers( request: Request ):
    # rows = session.query(User).all()
    resp = [
        {
            "id": row.id,"name": row.name,"email": row.email
        } for row in session.query(User).all()
    ]
    return JSONResponse( resp )

async def setUser( request: Request ):
    payload = await request.json()
    try:
        user = User(
            name=payload["name"],
            email=payload["email"],
            passwd=payload["passwd"]
        )
        session.add(user)
        session.commit()
        return JSONResponse({"msg": "usuario criado com sucesso"})
    except Exception as e:
        return JSONResponse({"err": str(e)})