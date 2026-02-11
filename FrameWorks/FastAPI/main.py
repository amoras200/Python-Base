from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {"Mude a url para": "/api/hello , /api/restaurantes/ ou /api/restaurantes?restaurante=nome_do_restaurante"}

@app.get("/api/hello")
def read_root():
    return {"Hello": "World"}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    url = 'https://amoras200.github.io/API-restaurante/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {"Dados": dados_json}

        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "preco": item['price'],
                    "descricao": item['description']
                })
        return {"Restaurante": restaurante, "Cardapio": dados_restaurante}
    else:
        return{'Erro': f'Erro ao acessar a API: {response.status_code} - {response.text}'}
