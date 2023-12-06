import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from starlette.status import HTTP_201_CREATED

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})

@app.get("/")
def read_root():
    return {"message": "Welcome from the API backend"}

@app.post("/create/{key}", status_code=HTTP_201_CREATED)
async def post_endpoint(key: str, value: str):
    return {"name": "test"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8081)