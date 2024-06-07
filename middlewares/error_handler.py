from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse


class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)
    
    #Método para deterctar si ocurre un error en nuestra aplicación, si no ocurre nada se ejecuta la próxima llamada si no hay error (call_next), en el caso de que haya un error se ejecutará JSONResponse
    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except Exception as e:
            return JSONResponse(status_code=500, content={'error': str(e)})