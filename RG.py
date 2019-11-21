from requests import get
from extract import extract
from bs4 import BeautifulSoup
import json
import art

print("_"*30)
art.tprint("RefG")
print('\033[7m' + "by GuTessitore" + '\033[0m')
print("‾"*30)
year = input("enter a year: ")

with open("links.json") as links:
	urls = json.load(links)

for url in urls["links"]:

	try:
		html = get(url).content
		content = BeautifulSoup(html, 'html.parser')

		titulo = extract.Titulo(content)
		nome = extract.Nome(url)

		data = extract.Data(year)

		reference = extract.Reference(titulo, nome, url, data)

		print(reference)
		print("\n")

	except:
		print('\033[31m' + "error: page not found <", url, ">" + '\033[0m')


