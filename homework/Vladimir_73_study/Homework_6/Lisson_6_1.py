''' text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl,
facilisis vitae semper at, dignissim vitae libero"
'''
# print(text)
# for x in text:
# print(x)
# print(text[22:26])
# print(text[22:26]+'ing')
# print(text[57:60]+'ing')
# print(text[75:79]+'ing')
# print(text[104:106]+'ing')
# e = (text[22:26]+'ing')
# ('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w')==text
# e = str("{e} + {'ing'}")
# print(text)

# text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
# words = text.split()
# print(words) # Разделяем текст на слова
# Вижу слова со знаками препинания


'''# Проверяем последний символ
word = "erat,"
print(f"Последний символ: '{word[-1]}'")
print(f"Знаки перед символом: '{word[:-1]}'")
new_word = word[:-1] + 'ing' + ','
print(new_word)
if word[-1] == ',':  # Если последний символ запятая
    result = word[:-1] + 'ing' + ','
elif word[-1] == '.':  # Если последний символ точка
    result = word[:-1] + 'ing' + '.'
else: #Обычное слово
    result = word + 'ing'
    print(f"Было: '{word}', Стало:'{result}'")
'''


'''word_1 = "vel."
print(f"Последний символ: '{word_1[-1]}'")
print(f"Знаки перед символом: '{word_1[:-1]}'")
new_word_1 = word_1[:-1] + 'ing' + '.'
print(new_word_1)

word_2 = "nisl,"
print(f"Последний символ: '{word_2[-1]}'")
print(f"Знаки перед символом: '{word_2[:-1]}'")
new_word_2 = word_2[:-1] + 'ing' +','
print(new_word_2)

word_3 = "at,"
print(f"Последний знак: '{word_3[-1]}'")
print(f"Знаки перед символом: '{word_3[:-1]}'")
new_word_3 = word_3[:-1] + 'ing' +','
print(new_word_3)
'''

# 1. Функция для одного слова


def add_ing(word):
    if word[-1] == ',':
        return word[:-1] + 'ing' + ','
    elif word[-1] == '.':
        return word[:-1] + 'ing' + '.'
    else:
        return word + 'ing'


# 2. Исходный текст
text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel."
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
print(f"Дан текст:{text}")
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
