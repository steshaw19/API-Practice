import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get('/test/calculate')
def calculate():
    return "hello world"

uvicorn.run(api, port=8000, host='127.0.0.1')