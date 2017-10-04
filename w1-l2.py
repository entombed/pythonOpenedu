"""
Лаборатория
Считать несколько имен людей одной строкой, записанных латиницей, через пробел, например:
«Anna Maria Peter».
Вывести их одной строкой в порядке возрастания «Anna Maria Peter».
Вывести их одной строкой в порядке убывания «Peter Maria Anna».

Пример входных данных:
Anna Maria Peter

Пример выходных данных:
Anna Maria Peter
Peter Maria Anna
"""
inputStr = str(input())
listStr = inputStr.split()
listStr.sort()
print(" ".join(listStr))
listStr.reverse()
print(" ".join(listStr))