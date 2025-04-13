def decor(func):
    def wrapper(*args, **kwargs):
        print(f"Функция {func.__name__} вызвана с аргументами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@decor
def calculate_area(length, width):
    return f"Площадь прямоугольника: {length * width}"

try:
    entered_length = float(input("Длина прямоугольника: "))
    entered_width = float(input("Ширина прямоугольника: "))
    if entered_length <= 0 or entered_width <= 0:
        print("Длина и ширина должны быть больше нуля!")
    else:
        print(calculate_area(entered_length, entered_width))
except:
    print("Длина и ширина должны быть числами!")