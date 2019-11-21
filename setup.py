import os

try:
	import bs4
except:
	print("Trying to Install required module: bs4\n")
	os.system('python -m pip install bs4')


try:
	import requests
except:
	print("Trying to Install required module: requests\n")
	os.system('python -m pip install requests')


try:
	import json
except:
	print("Trying to Install required module: json\n")
	os.system('python -m pip install json')


try:
	import art
except:
	print("Trying to Install required module: art\n")
	os.system('python -m pip install art')



try:
	import datetime
except:
  	print("Trying to Install required module: datetime\n")
  	os.system('python -m pip install datetime')


try:
	import random
except:
  	print("Trying to Install required module: random\n")
  	os.system('python -m pip install random')

print('\033[32m' + "All modules installed." + '\033[0m')
print('\033[7m' + "Don't forget to setup 'links.json' file to have all links that will be referenced" + '\033[0m')




