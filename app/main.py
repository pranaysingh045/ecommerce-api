from fastapi import FastAPI,Request
from app.api.v1.router import api_router
from app.api.core.exception import AppError
from fastapi.responses import JSONResponse

app=FastAPI(title="E-comerce application")

@app.exception_handler(AppError)
async def app_error_handler(request:Request,exc:AppError):
    return JSONResponse(status_code=exc.status_code,content={"details":exc.details})
app.include_router(api_router,prefix="/api/v1")