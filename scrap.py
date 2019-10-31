from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('test.csv', 'w')
csv_writer = csv.writer(csv_file)

total_mn = 0
md = []


def getMnemonics(word, no_of_mnemonics):
    global total_mn
    global md
    src = requests.get('https://mnemonicdictionary.com/?word='+word).text
    data = BeautifulSoup(src, 'lxml')
    for mnemonic in data.find_all('div', class_='card mnemonic-card'):
        for content in mnemonic.find_all('div', class_='card-text'):
            md.append(content.text)
            print(md[total_mn])
        total_mn = total_mn+1
        if(total_mn >= no_of_mnemonics):
            break


cd = ['\n ta', 'na']
getMnemonics('abase', 3)
print(type(md[0]))
a = 'Tasfik'
b = md[1]
c = md[2]
print(md[0].replace('\n', ''))
csv_writer.writerow(['Abase', 'Meaning', md[0].replace(
    '\n', ''),  md[1].replace('\n', ''), md[2].replace('\n', '')])
