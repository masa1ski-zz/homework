user_input = input(str('Введите текст для проверки: '))
user_input = user_input.lower()

counter_a = 0
counter_b = 0

for letter in range(len(user_input)):
    if user_input[letter] == 'ч' or user_input[letter] == 'щ':
        if user_input[letter + 1] == 'я':
            counter_a += 1
    elif user_input[letter] == 'ж' or user_input[letter] == 'ш':
        if user_input[letter + 1] == 'ы':
            counter_b += 1
    else:
        continue
print('Проверка окончена:')
print('Количество ошибок на правило ча, ща: ', counter_a)
print('Количество ошибок на правило жи, ши: ', counter_b)

input()
