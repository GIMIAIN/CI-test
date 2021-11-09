from application import application
from application import app
if application == "Hello world":
    try:
        application = app
    except ZeroDivisionError as err:
        print("Ошибка - деление на 0")
else:
    test = "0"
