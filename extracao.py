import json

with open("quotes.json",encoding='utf-8') as quotes_json:
    quotes = json.load(quotes_json)

for i in quotes:
    texto = (i['text'])
    autor = (i['author'])
    tags = (i['tags']) 

    print(texto,autor,tags)
    
