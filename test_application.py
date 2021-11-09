from application import application
#from application import app
if application == "Hello world":
    try:
        application = 1/0
    except ZeroDivisionError as err:
        print("Ошибка - деление на 0")
else:
    test = "0"
