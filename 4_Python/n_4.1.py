# Задача 1
squares = [x ** 2 for x in range(1, 11)]
print(f"1. {squares}")

# Задача 2 
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
week = {day: i+1 for i, day in enumerate(days)}
print(f"2. {week}")

# Задача 3
libs = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
tags = {lib.lower() for lib in libs}
print(f"3. {tags}")

# Задача 4
numbers = [1, 3, 4, 87, 98, 15, 7, 4]
evens = [num for num in numbers if num % 2 == 0]
print(f"4. {evens}")

# Задача 5 
def factorial(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("Недопустимое значение для возведения в факториал!")
    return 1 if n <= 1 else n * factorial(n - 1)

facts = {i: factorial(i) for i in range(1, 6)}
print(f"5. {facts}") 