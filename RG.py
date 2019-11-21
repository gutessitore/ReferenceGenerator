from requests import get
from extract import extract
from bs4 import BeautifulSoup
import json
import art

art.tprint("RefG")

with open("links.json") as links:
	urls = json.load(links)

for url in urls["links"]:

	try:
		html = get(url).content
		content = BeautifulSoup(html, 'html.parser')

		titulo = extract.Titulo(content)
		nome = extract.Nome(url)

		reference = extract.Reference(titulo, nome, url, "Hoje")

		print(reference)
		print("\n")

	except:
		print("error: page not found", url)



