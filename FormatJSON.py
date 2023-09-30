# Операции с введением чисел в формате JSON (с pydantic BaseModel)

from fastapi import FastAPI  # Импортируем класс FastAPI из библиотеки FastAPI
from pydantic import BaseModel  # Импортируем BaseModel из библиотеки Pydantic для определения модели данных

app = FastAPI()  # Создаем экземпляр FastAPI для нашего веб-приложения


class OperationRequest(BaseModel):  # Определяем модель данных для запросов к API
    num1: float  # Первое число
    num2: float  # Второе число


# Маршрут для выполнения операции сложения
@app.post("/Сложение v2")
async def add_numbers(request: OperationRequest):
    result = request.num1 + request.num2  # Выполняем сложение чисел
    return {"result": result}  # Возвращаем результат в формате JSON


# Маршрут для выполнения операции вычитания
@app.post("/Вычитание v2")
async def subtract_numbers(request: OperationRequest):
    result = request.num1 - request.num2  # Выполняем вычитание чисел
    return {"result": result}  # Возвращаем результат в формате JSON


# Маршрут для выполнения операции умножения
@app.post("/Умножение v2")
async def multiply_numbers(request: OperationRequest):
    result = request.num1 * request.num2  # Выполняем умножение чисел
    return {"result": result}  # Возвращаем результат в формате JSON


# Маршрут для выполнения операции деления
@app.post("/Деление v2")
async def divide_numbers(request: OperationRequest):
    if request.num2 == 0:
        return {"error": "Делить на ноль нельзя"}  # Проверка деления на ноль
    result = request.num1 / request.num2  # Выполняем деление чисел
    return {"result": result}  # Возвращаем результат в формате JSON


# штука для надписи на главном экране
@app.get("/")
def read_root():
    return 'прописать /docs в конце адресной строки'
