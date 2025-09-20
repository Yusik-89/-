import math

def factorial():
    try:
        # Безопаснее использовать input() внутри блока try
        number_str = input("Введите положительное целое число: ")
        number = int(number_str)
        
        if number < 0:
            raise ValueError("Введено отрицательное число")
            
        result = math.factorial(number)
        print(f"Факториал {number} равен {result}")
    
    except ValueError as e:
        print(f"Ошибка: {e}. Нужно ввести положительное целое число.")
    except Exception as ex:
        print(f"Произошла непредвиденная ошибка: {ex}")

factorial()