

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]


def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for i, a in enumerate(strings, start=1):
            position = file.tell()
            file.write(a + '\n')
            strings_positions[(i, position)] = a
    return strings_positions


result = custom_write('text_7_2.txt', info)
for elem in result.items():
  print(elem)