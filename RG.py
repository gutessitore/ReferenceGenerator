from requests import get
from extract import extract
from bs4 import BeautifulSoup
import art

art.tprint("RefG")

urls = ["http://comex2b.blogspot.com/p/blog-page_21.html", 
        "http://www.grupoboticario.com.br/pt/nossas-marcas/Paginas/Inicial.aspx",
        "https://www.boticario.com.br/nossa-historia", 
        "http://marcas.meioemensagem.com.br/o-boticario/", 
        "https://www.inesul.edu.br/site/escola_negocios/documentos/boticario.pdf",
       "http://www.agr.gc.ca/eng/industry-markets-and-trade/international-agri-food-market-intelligence/reports/sector-trend-analysis-pet-food-trends-in-france/?id=1538496137531"]

for url in urls:
	try:
		html = get(url).content
		content = BeautifulSoup(html, 'html.parser')

		titulo = extract.Titulo(content)
		nome = extract.Nome(url)

		reference = extract.Reference(titulo, nome, url, "Hoje")

		print(reference)

	except:
		print("error: page not found", url)



