def custom_write(file_name, strings):
    strings_position = {}

    file = open(file_name, 'w', encoding='utf-8')
    for line_number, line in enumerate(strings, 1):
        cursor_position = file.tell()
        file.write(line + '\n')
        strings_position[(line_number, cursor_position)] = line

    return strings_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
