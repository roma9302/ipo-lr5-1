#списки для проверки 
str_gl = "аеёиоуыэюя"
str_sogl = "бвгджзйклмнпрстфхцчшщ"

sogl = 0  # Счетчик согласных
gl = 0    # Счетчик гласных

string = input("Введите текст для вывода его длины, количества гласных и согласных букв: ")
#подсчет длины
len_string = len(string)

for i in string.lower():  # Приводим строку к нижнему регистру
    if i in str_gl:
        gl += 1
    elif i in str_sogl:
        sogl += 1
#вывод ответа
print(f"Длина строки равна: {len_string}, количество гласных букв в строке равно: {gl}, количество согласных букв в строке равно: {sogl}")