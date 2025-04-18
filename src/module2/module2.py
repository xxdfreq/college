print("=== Конвертер температуры ===")
print("1. Цельсий → Фаренгейт")
print("2. Фаренгейт → Цельсий")

choice = input("Выберите опцию (1 или 2): ")

if choice == "1":
    celsius = float(input("Введите градусы Цельсия: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit:.1f}°F")
elif choice == "2":
    fahrenheit = float(input("Введите градусы Фаренгейта: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F = {celsius:.1f}°C")
else:
    print("Ошибка! Введите 1 или 2.")