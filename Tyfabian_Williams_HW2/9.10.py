#Tyfabian Williams
#2142655

import csv
filename = input()
with open(filename, 'r') as wordsfile:
    word_reader = csv.reader(wordsfile)
    for row in word_reader:
        word_list = row
no_duplicates = list(dict.fromkeys(word_list))
listlength = len(no_duplicates)

for i in range(listlength):
    print(no_duplicates[i], word_list.count(no_duplicates[i]))
