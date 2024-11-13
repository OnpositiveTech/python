def analyze_number(number):
    if number < 0:
        return False  # возвращает булево значение
    elif number == 0:
        return None  # возвращает None
    else:
        return str(number)  # возвращает строку

print(analyze_number(-5))  # Выведет: False
print(analyze_number(0))   # Выведет: None
print(analyze_number(5))   # Выведет: "5"
