
import json

computador_json = """{
    "Marca": "Dell",
    "Preço": 15000   
}"""



dados = json.loads(computador_json)

# salvando arquivo json
with open('computador.json', 'w', encoding= 'utf-8')as arquivo_json:
    json.dump(computador_json,arquivo_json)
# lendo um arquivo json

with open('computador.json', encoding= 'utf-8') as arquivo_json:
  string_json = json.load(arquivo_json) # aqui estou convertendo para de um arquivo json para string
  dicionario_computador_json = json.loads(string_json)  # transformando string para dicionario, facilita na leitura
  print(dicionario_computador_json['Marca'])  