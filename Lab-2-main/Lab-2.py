from itertools import product
from random import random


f = open('books-en.csv').readlines()
file = list()
for line in f[1:]:
    file.append(line.split(';'))


Result_file = open('Generator.txt', 'w')

# №1 Вывести количество записей, у которых в поле -Название- строка длиннее 30 символов.
# №2 Реализовать поиск книги по автору, использовать ограничение на выдачу в зависимости от варианта. Вариант 4 - До 200 рублей

count_line_headline = 0
Author = input('Введите автора, которого хотите найти: ').lower()
list_BookAuthor = []
Count_generator = 0

for line in file:
    if len(line[1]) > 30:
        # print(line[1])
        count_line_headline += 1
    if line[2].lower() == Author and  float(line[-1].replace(',', ".")) < 200:
        list_BookAuthor.append(line[1])
    if Count_generator < 20:
        Result_file.write(f'{Count_generator + 1} {line[2]}. {line[1]} - {line[-4]}\n')
        Count_generator += 1

Result_file.close()

print(f'№1 Количество записей, у которых в поле -Название- строка длиннее 30 символов: {count_line_headline}')
print(f"""
№2 Поиск книги по автору: {Author.title()}:""")
for i in list_BookAuthor:
    print(i)