from fastapi import FastAPI
from starlette.responses import PlainTextResponse

app = FastAPI()

@app.get("/health")
async def health_check():
    return PlainTextResponse("건강합니다", status_code=200)

@app.get("/")
async def cicd_check():
    return PlainTextResponse("cicd success", status_code=200)

