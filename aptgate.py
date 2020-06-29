import os
import random
import requests

try:
	os.remove('temp.pdf')
except:
	pass
try:
	os.remove('temp.txt')
except:
	pass


icao='OKBK'
url = f'http://charts.avbot.in/{icao}.pdf'
r = requests.get(url, allow_redirects=True)
open('temp.pdf', 'wb').write(r.content)
os.system('pdf2txt.py temp.pdf>temp.txt')	#pip install pdfminer
with open('temp.txt') as f:
	result=f.readlines()
	maxrand=len(result)

standfound=False
while standfound==False:
	lineno=random.randint(0,maxrand-1)
	words=result[lineno].split()
	try:
		a=words.index('stand')
		print(words[a+1])
		standfound=True
	except:
		pass

try:
	os.remove('temp.pdf')
except:
	pass
try:
	os.remove('temp.txt')
except:
	pass
