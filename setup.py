import platform
import os

running_os = platform.system()

try:
	import pip
except:

	if running_os == "Linux":
		install = input("Do you want to install pip? [y/n]: ")
		if install == "y":
			os.system('sudo apt update')
			os.system('sudo apt install python3-pip')
		else:
			exit()

	elif running_os == "Windows":
		pass

	elif running_os == "Darwin":
		pass

	else:
		print('\033[31m' + "Can't find operating system" + '\033[0m')

try:
	import bs4
except:
	print('\033[33m' + "Trying to Install required module: bs4\n" + '\033[0m')
	os.system('python -m pip install bs4')


try:
	import requests
except:
	print('\033[33m' + "Trying to Install required module: requests\n" + '\033[0m')
	os.system('python -m pip install requests')


try:
	import json
except:
	print('\033[33m' + "Trying to Install required module: json\n" + '\033[0m')
	os.system('python -m pip install json')


try:
	import art
except:
	print('\033[33m' + "Trying to Install required module: art\n" + '\033[0m')
	os.system('python -m pip install art')



try:
	import datetime
except:
  	print('\033[33m' + "Trying to Install required module: datetime\n" + '\033[0m')
  	os.system('python -m pip install datetime')


try:
	import random
except:
  	print('\033[33m' + "Trying to Install required module: random\n" + '\033[0m')
  	os.system('python -m pip install random')

try:
	import tqdm
except:
  	print('\033[33m' + "Trying to Install required module: tqdm\n" + '\033[0m')
  	os.system('python -m pip install tqdm')

print('\033[32m' + "All modules installed." + '\033[0m')
print('\033[33m' + "Don't forget to setup 'links.json' file to have all links that will be referenced" + '\033[0m')




