from bs4 import BeautifulSoup
from extract import extract
from requests import get
from tqdm import tqdm
import json
import art

print("_"*30)
art.tprint("RefG")
print('\033[7m' + "by GuTessitore" + '\033[0m')
print("‾"*30)
year = input("enter a year: ")

output = '''
<!DOCTYPE html>
<html>
<head>
<title>Reference generator</title>
</head>
<body style="background-color: #f8f8f8;
margin: 0;
padding: 0;
border: 0;">

<div style="background-color: #e7e7e7;
width: 100%;
height: 3em;">
</div>

<div style="margin-left: auto;
margin-right: auto;
width: 18em;
font-size: 2em;">
<h1 style="margin: 0; ">Reference Generator</h1>
</div>

<div style="padding: 10px;">
<div>
'''

with open("links.json") as links:
	urls = json.load(links)

for url in tqdm(urls["links"]):

	try:
		html = get(url).content
		content = BeautifulSoup(html, 'html.parser')

		titulo = extract.Titulo(content)
		nome = extract.Nome(url)

		data = extract.Data(year)

		reference = extract.Reference(titulo, nome, url, data)

		# print(reference)
		# print("\n")

		output += "<p>" + reference + "</p>"

	except:
		print('\033[31m' + "error: page not found <" + url + ">" + '\033[0m' + "\n")

output += '''
</div>
</div>

</body>
</html>
'''

html_file = open("page.html", "w")
html_file.write(output)
html_file.close()