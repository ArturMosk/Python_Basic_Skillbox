family_members = {
    ('Иванов', 'Иван'): 45,
    ('Петров', 'Петр'): 26,
    ('Сидоров', 'Никита'): 35,
    ('Иванова', 'Светлана'): 33,
    ('Петрова', 'Нина'): 23,
    ('Сидорова', 'Алина'): 34,
    ('Иванов', 'Алексей'): 15,
    ('Петров', 'Роман'): 6,
    ('Сидоров', 'Павел'): 10
}

family = input('Введите фамилию: ').lower()

print()
for i_key, i_value in family_members.items():
    if i_key[0].lower().startswith(family[:-1]):
        print(i_key[0], i_key[1], i_value)