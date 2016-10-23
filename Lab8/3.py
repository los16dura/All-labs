import string
import codecs
words_counter = {}
s = ''
m = []
file = codecs.open(r'C:\Users\euroset\AppData\Local\Programs\Python\Python35-32\LICENSE8.txt', 'r' , encoding='utf-8')
f = [x for x in file.read()]
for i in range(len(f)):
    if f[i] in string.punctuation:
        f[i] = ' '
    s = s + f[i] ;
words = s.split()
#print(m)

for i in range (len(words)):
    if words[i] not in words_counter:
        words_counter[words[i]] = 1
    else:
        words_counter[words[i]] += 1

for i in range (10):
    str = list(words_counter.values())
    maks = str.index(max(str))
    t = list (words_counter.keys())
    print(t[maks])
    del words_counter[t[maks]]
file_output = open('output.txt', 'w')
