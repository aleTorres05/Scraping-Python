from bs4 import BeautifulSoup
from pprint import pp
from typing import List, Optional
from re import search
import httpx
import json

"""ES NECESARIO HACER UNO A LA VES POR LA CANTIDAD ASENTAMIENTOS QUE SON"""

def obtener_nombre_url(url: Optional[str] = "https://micodigopostal.org/"):
    referencias = []
    anuncios = []

    page = httpx.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find("tbody")
    
    for tr in table:
        for td in tr:
            for a in td:
                try:
                    referencias.append(a["href"])
                except:
                    anuncios.append(a)
    return referencias


def obtener_url_completa_estados(url: Optional[str] = "https://micodigopostal.org/") -> List[str]:
    referencias = obtener_nombre_url()
    url_completa = []

    for estado in referencias:
        url_completa.append(url + estado[1:])
    return url_completa


def obtener_url_completa_municipios(url: Optional[str] = "https://micodigopostal.org/") -> List[str]:
    url_completa = obtener_url_completa_estados()
    url_completa_municipios =  []
    for url_estados in url_completa:
        referencias = obtener_nombre_url(url_estados)
    
        for municipio in referencias:
            url_completa_municipios.append(url + municipio[1:])
            
    return url_completa_municipios


def obtener_codigo_postal():
    url_municipios = obtener_url_completa_municipios()
    municipios = obtener_nombre_url()
    codigos_postales = []
    resultado = []
    lista_municipios = []
    string = "https://micodigopostal.org/zacatecas/"
    estados = []

    for municipio in municipios:
        lista_municipios.append(municipio.replace("/", ""))

    for url in url_municipios:
        if search(string, url):
            estados.append(url)

    for url_estados in estados:
        page = httpx.get(url_estados)
        soup = BeautifulSoup(page.content, "html.parser")
        table = soup.find("tbody")

        for tr in table.find_all("tr"):
            if len(tr) > 4:
                codigo_postal = [td.text for td in tr.find_all("td") if tr != []]
                codigos_postales.append(codigo_postal)
                resultado.append({
                    "municipio": codigo_postal[3],
                    "estado": lista_municipios[31],
                    "ciudad": codigo_postal[4],
                    "asentamiento": codigo_postal[0],
                    "tipo_asentamiento": codigo_postal[1],
                    "codigo_postal": codigo_postal[2]
                })

    return resultado


with open("codigos_postales_zacatecas.json", "w", encoding="utf-8") as file:
    json.dump(obtener_codigo_postal(), file)




