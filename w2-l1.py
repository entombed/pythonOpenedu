'''
Считать отдельными операторами целочисленные ширину и высоту прямоугольника. Создать функцию (def), принимающую в качестве параметров ширину и высоту фигуры и название функции, которую необходимо выполнить. Имя вложенной функции передавать явным образом (например: (a,b,name='perim')).
Внутри функции создать две вложенные функции (def) по подсчету площади и периметра фигуры. Вывести одной строкой через пробел площадь и периметр, разделенные пробелом (например, '20 18').

Пример входных данных:
4
5

Пример входных данных:
20 18 
'''
x = int(input())
y = int(input())

def rez(x, y, name='perim'):
    def perim(x,y):
        return (2*(x + y))
    def square(x,y):
        return (x*y)
    if name == 'perim':
        return perim(x,y)
    elif name == 'square':
        return square(x,y)

s = rez(x, y, 'square')
p = rez(x, y, 'perim')
print(s, p)