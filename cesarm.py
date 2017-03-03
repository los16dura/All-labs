

class Caesar:
    alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

    def __init__(self, key):
        self._encode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i + key) % len(self.alphabet)]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()
        self._decode = {v: k for k,v in self._encode.items()} # sintaxis for dict

        #for k, v in self._encode.items():
        #    self._decode[v] = k
        #(another variant)

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, text):
        return ''.join([self._dencode.get(char, char) for char in text])


key = int(input('Введите ключ:'))
cipher = Caesar(key)
line = input()
while line!='.':
    print(cipher.encode(line))
    line = input()