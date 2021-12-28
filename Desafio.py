#Entrada
#Fornecemos um catálogo de produtos em anexo ("catalogo_produtos.json") que é um arquivo que possui, em cada linha, um produto no formato JSON.

import json
from operator import contains, itemgetter

JSON_FILE_PATH = "catalogo_produtos.json"
produto = input('Digite aqui sua consulta:')
contador = 0

with open(JSON_FILE_PATH, "r", encoding="utf8") as json_file:

    json_data = json.load(json_file)

    for input_ in json_data["Produtos"]:

        id = input_["id"],
        name = input_["name"]

        if(produto.title() in input_["name"]):
            print(sorted(id), name)


# Saída
# O programa deverá esperar consultas serem enviadas via linha de comando e encontrar os produtos que são relacionados com estas consultas.
# Limite a saída a, no máximo, 20 resultados ordenados por ID em ordem crescente.

#> ./processador
#> Digite aqui sua consulta: perfume
#1 - "ID" - "Nome do Produto"
#2 - "ID" - "Nome do Produto"
#3 - "ID" - "Nome do Produto"

# para order use o variavel.sort()