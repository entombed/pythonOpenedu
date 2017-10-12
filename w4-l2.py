'''
Считать одной строкой произвольное количество пар элементов "Название книги Число экземпляров", второй строкой название алгоритма хеширования md5
Aibolit 66 Barmaley 67
md5

Создать 2 класса:
1-й преобразует строку вида 'Aibolit 66 Babmaley 67', где название книги уникально, в словарь.
2-й осуществляет хеширования названия книги алгоритмом md5.
Вывести отдельными операторами вывода:
- элементы словаря, отсортированные по возрастанию ключа, например:
Aibolit 66
Barmaley 67
- результаты хеширования в виде пар названия алгоритма и результатов хеширования ключей, отсортированных по возрастанию, представленных в шестнадцатеричном виде, сведенных в одну строку через пробел вида
md5 c47.... md5 5d....' (без пробелов в начале и конце строки).

Пример входных данных:
Aibolit 66 Barmaley 67
md5

Пример выходных данных:
Aibolit 66
Barmaley 67
md5 768414e20f688934976716d717e7986b md5 96b0e4c581d12e5014c6b443e770c460
Вариант

'''
import hashlib
class createDict(object):
    def __init__(self, inStr, hashAlg):
        self.inStr = inStr
        self.hashAlg = hashAlg
        inList = inStr.split()
        self.inDict = dict(zip(inList[::2], inList[1::2]))
        for item in sorted(self.inDict.keys()):
            print(item, self.inDict[item])

class makeHash(createDict):
    def doHash(self):
        rezStr = ''
        tmpList = []
        inHash = hashlib.new(self.hashAlg)
        for val in self.inDict:
            inHash.update(val.encode())
            rezHash = inHash.hexdigest()
            tmpList.append(rezHash)
        for item in sorted(tmpList):
            rezStr += '{} {} '.format(self.hashAlg, item)
        return rezStr.strip()


#inStr = 'Maugli 55 Contakt 49 Qwerty 111 Qwerty 222 Aibolit 66 XXX 65'
#inDict = {'Maugli': '55', 'Contakt': '49', 'Qwerty': '222', 'Aibolit': '66', 'XXX': '65')
#hashAlg = 'md5'
#inDict = {}
inStr = str(input())
hashAlg = str(input())



x = makeHash(inStr, hashAlg)
print(x.doHash())
