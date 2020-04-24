import random


sufx = []

l = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
n = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м',
     'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']

for i in l:
    for j in n:
        x = j + i
        sufx.append(x)

norm_word = 'пошли гулять на улицу в футбол'
norm_word = norm_word.split()

transform_word = []

for i in norm_word:
    trans_word = i[1::] + i[0] + random.choice(sufx)
    transform_word.append(trans_word)

print(*transform_word)