# 1. Функция для одного слова


def add_ing(word):
    if word[-1] == ',':
        return word[:-1] + 'ing' + ','
    elif word[-1] == '.':
        return word[:-1] + 'ing' + '.'
    else:
        return word + 'ing'


# 2. Исходный текст
text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
print(f"Дан текст: {text}")
# 3. Разбиваем на слова
words = text.split()
print(f"Исходные слова: {words}")

# 4. Преобразуем каждое слово
new_words = []
for word in words:
    new_word = add_ing(word)
    new_words.append(new_word)

print(f"Новые слова: {new_words}")

# 5. Собираем обратно в текст
new_text = " ".join(new_words)
print(f"Новый текст: {new_text}")
