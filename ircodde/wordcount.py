import xml.etree.ElementTree as ET
import re
f4 = open("wordCount.txt", 'w')
text = ''
filelist=[]
filelist.append("hindi-document-00001.txt")
filelist.append("hindi-document-00002.txt")
filelist.append("hindi-document-00003.txt")
for filename in filelist:
	tree = ET.parse(filename)
	root = tree.getroot()
	for i in root.findall('title'):
		text1 = i.text
	for i in root.findall('content'):
		text2 = i.text
	text = text + text1 + text2
	text = text.replace("॥"," ");
	text = text.replace("।"," ");
	text = text.replace(":"," ");
	text = text.replace(","," ")
	text = text.replace("?"," ");
	text = text.replace("-"," ");
	text = text.replace("\\n"," ");
	word = text.split(" ")
        
	l = set(word)
	wordUnique = list(l)
for i in range(len(wordUnique)):
	f4.write(str(wordUnique[i]) + '\t\t\t')
	f4.write(str(word.count(str(wordUnique[i]))) + '\n')


	
