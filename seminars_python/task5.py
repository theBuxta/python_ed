# Напишите программу, удаляющую из текста все слова содержащие "абв".

text = 'Из этого абв текста будут удалены все "абв" слова ?'
print(text)

def abv_filter(text):
    text = list(filter(lambda a: 'абв' not in a, text.split()))
    return " ".join(text)

text = abv_filter(text)
print(text)
print('?')