import string
import codecs
file = codecs.open(r'en-ru.txt', 'r' , encoding='utf-8')#ткрываем файл
f = file.readlines()#считываем построчно

dictionary = {}
for i in f:
    i = i.rstrip()#удаляем из каждой строки /n
#print(f[:3])
for i in f:
    k, v = i.split('\t-\t')
    v = v.rstrip()
    dictionary[k] = v
print(dictionary)
input = codecs.open(r'input.txt', 'r' , encoding='utf-8')
outputfile = codecs.open('output.txt', 'w')
inp = input.readlines()
n = []
for i in inp:
    n = i.split(' ')
    for j in n:
        if  not j.isalnum():
            #print('!!!!!',j)
            znak = j[-1]
            j = j[:-1]
        else:
            znak = ''
            #output.write\
        if j in dictionary:
             print(dictionary[j],znak,end = '') # через write
        else:
             print(j,znak,end = '')
    print(end='')
