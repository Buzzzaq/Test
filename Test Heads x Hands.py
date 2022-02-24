import random
def function(n):
    result = []

    # Генерация списка рандомных чисел
    l1 = random.sample(range(1, n+10), n)

    # Генерация вложенного списка случайого размера
    for i in range(n):
        l2 = []
        result.append(l2)
        for j in range(l1[i]):
            l2.append(random.randint(1, 99))

    # Сортировка списка с четным порядковым номером по возрастанию, с нечетным - по убыванию
    for i in range(len(result)):
        if i % 2 == 0:
            result[i].sort()
        else:
            result[i].sort(reverse=True)
    return result

print(function(int(input("Введите число: "))))
