# coding=UTF-8
filename = raw_input('檔名：')
f = open(filename, 'r')
b_str = f.read()
f.close()
print b_str.decode('utf-8') # what's this?
print b_str.decode('utf-8').encode('utf-8') # what's this?