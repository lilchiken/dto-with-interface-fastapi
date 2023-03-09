from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from dto.responsedto import ResponseDTO
from responses.response import response_now
from responses.response import response_forecast

# Наше приложение FastAPI
app = FastAPI()

# Подключаем статику для красоты
app.mount('/static', StaticFiles(directory='static'), name='static')


# Подключаем Jinja2 для рендера темплейта, в нашем случае одного
templates = Jinja2Templates(directory='templates')


@app.post('/now')
def now(
    token: str = Form(),
    location: str = Form()
) -> JSONResponse:
    """Генерим JSON из форм с main страницы."""
    response = response_now(
        token,
        location
    )
    return JSONResponse(jsonable_encoder(ResponseDTO(response)))


@app.post('/forecast')
def forecast(
    token: str = Form(),
    days: str = Form(),
    location: str = Form()
) -> JSONResponse:
    """Генерим JSON из форм с main страницы."""
    response = response_forecast(
        token,
        days,
        location
    )
    return JSONResponse(jsonable_encoder(ResponseDTO(response)))


@app.get('/')
def main(request: Request):
    """Генерим html при помощи Jinja2."""
    return templates.TemplateResponse('index.html', {'request': request})
