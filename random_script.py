import random
class Monoalphabet:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, keytable):
        lowercase_code = {x: y for x, y in zip(self.alphabet, keytable)}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, keytable)}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
        self._decode = {'э':'а','ь':'б','о':'в','р':'г','м':'д','щ':'е','н':'ж','й':'з','г':'и','й':'','к':''}

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, text):
         return ''.join([self._dencode.get(char, char) for char in text])





key = Monoalphabet.alphabet[:]
key_list = [x for x in key]
random.shuffle(key_list)
cipher = Monoalphabet(key_list)
line = input()
while line!='.':
    print(cipher.encode(line))
    line = input()
