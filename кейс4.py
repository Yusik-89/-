import random

def guess_number_game():
    # Генерируем случайное число от 1 до 100
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5  # Ограничиваем количество попыток

    print("Привет! Давай сыграем в 'Угадай число'. Я загадал число от 1 до 100.")
    
    while True:
        try:
            user_guess = int(input(f"У тебя {max_attempts - attempts} попытки(-ок). Твой вариант числа: "))
            
            if user_guess > number:
                print("Слишком большое число!")
            elif user_guess < number:
                print("Слишком маленькое число!")
            else:
                print(f"Правильно! Ты угадал число {number}.")
                break
        
            attempts += 1
            if attempts >= max_attempts:
                print(f"К сожалению, твои попытки закончились. Загаданное число было {number}.")
                break
                
        except ValueError:
            print("Введено некорректное значение. Введите целое число.")

if __name__ == "__main__":
    guess_number_game()
