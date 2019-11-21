from requests import get
from bs4 import BeautifulSoup

class extract(object):

    def __init__(self):
        pass

    def Titulo(content):
        try:
            titulo = content.title.text.strip()
        except:
            titulo = "Sem título"
        return(titulo)

    def Nome(url):
        #Get name before .com or .org or .edu
        if url.split(".")[2] == "com" or url.split(".")[2] == "org" or url.split(".")[2] == "edu":
            nome = url.split(".")[1].upper()
        else:

                        #test for https
            if url.split(".")[0][0:5] == "https":
                #If after the https is www get the second name after the "."
                if url.split(".")[0][8:] != "www":
                    nome = url.split(".")[0][8:].upper()
                else:
                    nome = url.split(".")[1].upper()

            #check if it is http
            elif url.split(".")[0][0:4] == "http": 
                #If after the http is www get the second name after the "."
                if url.split(".")[0][7:] != "www":
                    nome = url.split(".")[0][7:].upper()
                else:
                    nome = url.split(".")[1].upper()
            
        return(nome)

    def Data(start, end):
        #format '%d %b. %Y.'
        pass

    def Reference(titulo, nome, url, data):
        reference = str( nome.upper() + ". " + titulo + ". Disponível em: " + url + ". Acesso em: " + data)
        return(reference)










