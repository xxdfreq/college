import random

print("=== Угадай число от 1 до 10 ===")
secret_number = random.randint(1, 10)  # Компьютер загадывает число

while True:
    try:
        guess = int(input("Твоя догадка: "))  # Пользователь вводит число
    except ValueError:
        print("Ошибка! Введите число от 1 до 10.")
        continue

    if guess < 1 or guess > 10:
        print("Число должно быть от 1 до 10!")
    elif guess < secret_number:
        print("Загаданное число больше!")
    elif guess > secret_number:
        print("Загаданное число меньше!")
    else:
        print(f"Поздравляю! Ты угадал число {secret_number}!")
        break