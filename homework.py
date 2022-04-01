# #7.1 Создайте 2 кортежа с 10 случайными числами от -5 до 0. Объедините их и посчитайте
# # # сколько раз в получившемся кортеже встретится 0
# #
import random


a = tuple(random.randint(-5, 0) for i in range(10))
b = tuple(random.randint(-5, 0) for i in range(10))
c = a + b
print(c)
print(c.count(0))
# #
# #
# # # 7.2 Создайте кортеж из 5 случайных чисел от 1 до 10. Все числа, кроме первого и
# # # последнего, распаковать в один список. Для распаковки используйте *
import random


nums = tuple(random.randint(1, 10) for i in range(5))
nums_s = nums[1:4]
a, b, c = nums_s
print(a, b, c, sep=',')

# 7.3 На вход программе подаются числа. Создайте кортеж из чисел меньше 5
import random


a = tuple(random.randint(1, 15) for i in range(5))
num = tuple()
for i in a:
    if i < 5:

else:
    print('попробуй ещё')
print(num)

# 7.4 У вас есть кортеж, который содержит список. Измените кортеж так, чтобы список был
# пустым.

tpl = (12, 31, [11, 5, 6, 4])
tpl[2][0:4] = ' '
print(tpl)

#
#
# # 9.1 На вход программа принимает 2 строки и выводит их общие символы
#
srt_0 = {1, 5, 2, 35, 5, 3, 5, 6}
srt_1 = {5, 6, 3, 1, 45, 3, 1, 5}
set_1 = srt_0 & srt_1
print(set_1)