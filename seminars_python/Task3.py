from random import*

list = [randint(1, 11) for i in range(1, 11)]
list1 = []
print(f"Дана последовательность: {list}")
for i in list:
    if list.count(i) == 1:
        list1.append(i)
print(f"Неповторяющиеся элементы последовательности: {list1}")