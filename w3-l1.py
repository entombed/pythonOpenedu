'''
Лаборатория
Ввести с клавиатуры строку латиницей (1-3 слова). Зашифровать ее с использованием гарантированных алгоритмов шифрования. Сформировать словарь, где в качестве ключа используется название гарантированного алгоритма шифрования, а в качестве значения - результат шифрования в шестнадцатеричном представлении { 'sha1': 'd0b…', 'md5', '1f3…',…}.
Итог вывести отдельными операторами вывода в виде пар ключа и значения, отсортированных по возрастанию ключа:
md5 1f3…
sha1 d0b…

Пример входных данных:
apple

Пример выходных данных:
md5 1f3870be274f6c49b3e31a0c6728957f
sha1 d0be2dc421be4fcd0172e5afceea3970e2f3d940
sha224 b7bbfdf1a1012999b3c466fdeb906a629caa5e3e022428d1eb702281
sha256 3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b
sha384 3d8786fcb588c93348756c6429717dc6c374a14f7029362281a3b21dc10250ddf0d0578052749822eb08bc0dc1e68b0f
sha512 844d8779103b94c18f4aa4cc0c3b4474058580a991fba85d3ca698a0bc9e52c5940feb7a65a3a290e17e6b23ee943ecc4f73e7490327245b4fe5d5efb590feb2
'''
import hashlib

def makeHashDict (inStr):
    #hashTmp = {'md5', 'sha512', 'sha224', 'sha384', 'sha1'}
    hashTmp = hashlib.algorithms_guaranteed
    hashDict = {}
    for item in hashTmp:
        hashItem = hashlib.new(item)
        hashItem.update(inStr.encode())
        hashStr = hashItem.hexdigest()
        hashDict.update({item:hashStr})
    return hashDict

def printHashDict(hashDict):
    for key in sorted(hashDict.keys()):
        print(key, hashDict[key])

#inputStr = 'python'
inputStr = input()

printHashDict(makeHashDict(inputStr))