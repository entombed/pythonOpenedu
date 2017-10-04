'''
Лаборатория
Считать отдельными операторами целочисленные ширину и высоту прямоугольника, создать список из лямбда функций подсчета площади и периметра фигуры.
Вывести первым оператором индекс лямбда функции подсчета площади и ее результат (например:0 20);
вторым оператором индекс лямбда функции подсчета периметра и ее результат (например:1 18);
вывести третьим оператором список полученным значений (например: [20, 18]);
вывести четвертым оператором итоговые значения, сведенные в одну строк через пробел (например: '20 18').

Пример входных данных:
4
5

Пример выходных данных:
0 20
1 18
[20, 18]
20 18
'''
x = 4
y = 5
rezList = []
listFunctions = [lambda x,y:x*y, lambda x,y:2*(x+y)]
tmpDict = dict(enumerate(listFunctions))
for key, val in tmpDict.items():
    tmpRez = val(x,y)
    print(key, tmpRez)
    rezList.append(tmpRez)

print(rezList)

rezList = list(map(lambda item:str(item), rezList))
rezStr = ' '.join(rezList)
print(rezStr)