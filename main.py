import uvicorn
from fastapi import FastAPI
from src.prime_number import prime_router
from src.image_inversion import image_inversion_router
from src.auth import auth_router


app = FastAPI()
app.include_router(prime_router)
app.include_router(image_inversion_router)
app.include_router(auth_router)


@app.get('/')
def main_page():
    return 'All endpoints can be found at https://fastapi-projekt.herokuapp.com/docs. API Key for the 3rd endpoint is: abcd1234'


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
