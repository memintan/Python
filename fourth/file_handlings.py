import json
import csv
import os

path = '/Users/halilibrahimtan/Documents/Python/fourth/files/abc.txt'
path1 = '/Users/halilibrahimtan/Desktop/java'

text_file = open(path, 'r')
print(text_file.read())

# print(text_file.readline())

text_file1 = open(path1, 'r')
print(text_file1.read())

text_file.close()
text_file1.close()

print('---------------------------')

path = 'files/Test2.txt'

text_file2 = open(path, 'w')
text_file2.write('\n this is a new text file \n Python created this file')
text_file2.close()

os.remove(path)