'''
def writer():
    title = 'HackerEarth'
    name = (lambda x:title + ' ' + x)
    return name

w = writer()
print(w('Fremont'))
'''
from functools import reduce
hck = [5, 8, 10, 20, 50, 100]
total= reduce((lambda a, b: a+b), hck)
print(total)