""" Генерирование случайных чисел """
from random import random, sample
# sample() гарантирует уникальность генерации ранддомной последовательности

num = random()
print('Random float 0.0-1.0 :', num)
num = int(num * 10)
# приведение к целочисленному значению
print('Random integer 0-9 :', num)
nums = []
i = 0
while i < 6:
    """ Добавление цикла для множественного присваивания случайных целых элементов"""
    nums.append(int(random() * 10) + 1)
    i += 1
print('Random Multiple Integers 1-10 :', nums)
nums = sample(range(1, 49), 6)
    
print('Random Integer Sample 1-49 : ', nums)