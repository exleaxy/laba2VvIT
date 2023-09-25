# Операции с введением чисел в текстовые поля (без pydantic BaseModel)

from fastapi import FastAPI  # Импортируем класс FastAPI из библиотеки FastAPI

app = FastAPI()  # Создаем экземпляр FastAPI для нашего веб-приложения


# Определяем маршрут и функцию для сложения
@app.post("/Сложение")
def add(num1: float, num2: float):
    result = num1 + num2  # Вычисляем результат
    return {"result": result}  # Возвращаем результат в формате JSON


# Определяем маршрут и функцию для вычитания
@app.post("/Вычитание")
def subtract(num1: float, num2: float):
    result = num1 - num2  # Вычисляем результат
    return {"result": result}  # Возвращаем результат в формате JSON


# Определяем маршрут и функцию для умножения
@app.post("/Умножение")
def multiply(num1: float, num2: float):
    result = num1 * num2  # Вычисляем результат
    return {"result": result}  # Возвращаем результат в формате JSON


# Определяем маршрут и функцию для деления
@app.post("/Деление")
def divide(num1: float, num2: float):
    if num2 == 0:
        return {"error": "На ноль делить нельзя."}  # Проверяем, что num2 не равен нулю
    result = num1 / num2  # Вычисляем результат
    return {"result": result}  # Возвращаем результат в формате JSON


# штука для надписи на главном экране
@app.get("/")
def read_root():
    return 'прописать /docs в конце адресной строки'
