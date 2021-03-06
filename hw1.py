# 8.2 Программа принимает список из трех слов. Создать словарь, в котором ключ — слово,
# значение — количество символов в слове
ls0 = [input() for i in range(3)]
ls1 = [len(ls0[0]), len(ls0[1]), len(ls0[2])]
d = dict(zip(ls0, ls1))
print(d)

#  8.3 На вход подается список чисел. Создать словарь, в котором ключ — число, значение —
# число на 10% больше. Значение должно быть округленное.
import random


ls0 = [random.randint(0, 100) for i in range(5)]
ls1 = [ls0[0] + (ls0[0] / 10), ls0[1] + (ls0[1] / 10),
       ls0[2] + (ls0[2] / 10), ls0[3] + (ls0[3] / 10),
       ls0[4] + (ls0[4] / 10)]
d = dict(zip(ls0, ls1))
print(d)


#  8.6 Создать словарь, который в качестве ключа будет использовать страну, а в качестве
# значения - ее столицу. Внеси в него следующие страны: Россия (Москва), Украина
# (Киев), Италия (Рим), Испания (Мадрид), Болгария (София).
# Программа должна запрашивать у пользователя, столицу какой страны он хочет узнать
# и выдавать результат.
contry = ['Россия', 'Украина', 'Италия', 'Испания', 'Болгария']
city = ['Москва', 'Киев', 'Рим', 'Мадрид', 'София']
d = dict(zip(contry, city))
contry1 = input('Введите название страны столицу каторой вы хотите узнать: ').capitalize()
for k, v in d.items():
    if contry1 == k:
        print(k, '-', v)

# 8.7 Создать словарь, ключи — числа, значения — слова. Удалить из него все
# пары с нечетными ключами. Вывести на печать
# В этом вам может помочь статья, что сбрасывала ранее.
import random


ls0 = [random.randint(0, 100) for i in range(4)]
ls1 = [input() for i in range(4)]
d = dict(zip(ls0, ls1))
new_dict = {k: v for k, v in d.items() if not k % 2}
print(d)
print(new_dict)



# 10.1 Создать список из 10
# случайных чисел.
# Записать в файл:
# 1.Количество элементов в
# списке
# 2. Все элементы списка в одну
# строку
# Т.е. в файле должно быть 2
# строки
import random


nums = [random.randint(0, 100) for i in range(10)]

with open('file.txt', "w") as f:
    f.write(str(len(nums)) + '\n')

    for i in nums:
        f.write(str(i) + ' ')


# 10.2 Прочитать из файла числа,
# сформировать список и
# напечатать его
line1 = []
with open('file.txt', 'r') as file:
    line = [file.readlines()]
    line1 += line
print(line)
print(line1)
# по этому заданию вопрос как убрать \n в выводе ?



