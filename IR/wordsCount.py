from lxml import etree
import os
import glob
file = open("lab1Result/wordCount.txt","w")
stopWords = [line.rstrip('\n') for line in open('stopWords.txt')]
file.write("word\t\tcount\n")
path = 'docs'
words=[]
wordCounts={}

for infile in glob.glob( os.path.join(path, '*.txt') ):
	a=etree.parse(infile)
	titlef=a.find('title').text
	contentf=a.find('content').text
	b = "!,-।1234567890-()॥:"
	for char in b:
		titlef = titlef.replace(char,"")
		contentf=contentf.replace(char,"")
	titleWord=titlef.split()
	contentWord=contentf.split()
	words=words+titleWord+contentWord
uniqueWords=list(set(words))
for word in uniqueWords:
    if word not in stopWords:
        wordDict={word:words.count(word)}
        wordCounts.update(wordDict)
for i in wordCounts.keys():
	file.write(str(i)+"\t\t"+str(wordCounts[i])+"\n")
file.close()
