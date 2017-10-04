'''
Лаборатория
Считать отдельными операторами целочисленные ширину и высоту прямоугольника, создать функцию (def), принимающую в качестве параметров ширину и высоту фигуры.
Внутри функции создать две вложенные функции (lambda) по подсчету площади и периметра фигуры. Вывести одной строкой через пробел площадь и периметр, разделенные пробелом (например '20 18').

Пример входных данных:
4
5

Пример выходных данных:
20 18
'''
x = int(input())
y = int(input())


def fun (fx, fy):
    s = lambda fx, fy: fx*fy
    p = lambda fx, fy: 2*(fx+fy)
    return [str(s(fx, fy)), str(p(fx, fy))]
print(' '.join(fun(x, y)))