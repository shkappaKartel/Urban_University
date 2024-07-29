from pprint import pprint

name = 'sample.txt'
file = open(name, 'r')
pprint(file.read())
file.close()


file1 = 'sample1.txt'
file = open(file1, 'w')
file.write('text from terminal')
file.close()

file = open(file1, 'r')
pprint(file.read())
file.close()


def file_reader(fn):
    file = open(fn, 'r')
    pprint(file.read())
    file.close()


file = open(file1, 'a')
file.write('\nnew row from terminal')
file.close()

file_reader(fn='sample.txt')
file_reader(fn='sample1.txt')

file = open(file1, 'r')
pprint(file.tell())
pprint(file.seek(7))
pprint(file.read())
file.close()
