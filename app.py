from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Permite requisições do frontend

# Função para buscar dados do CEP
def buscar_cep(cep):
    url = f'https://brasilapi.com.br/api/cep/v1/{cep}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {"error": "CEP não encontrado"}

# Função para buscar dados do IBGE (código do município)
def buscar_ibge(codigo_ibge):
    if not codigo_ibge:
        return {"error": "Código IBGE não informado"}
    
    url = f'https://brasilapi.com.br/api/ibge/municipios/v1/{codigo_ibge}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {"error": "Dados do IBGE não encontrados"}

# Função para buscar dados do DDD
def buscar_ddd(ddd):
    if not ddd:
        return {"error": "DDD não informado"}
    
    url = f'https://brasilapi.com.br/api/ddd/v1/{ddd}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {"error": "Dados do DDD não encontrados"}

# Endpoint principal
@app.route('/dashboard/<string:cep>')
def get_dashboard(cep):
    # Verifica se o CEP tem 8 dígitos
    if not cep.isdigit() or len(cep) != 8:
        return jsonify({"error": "CEP inválido. Deve conter 8 números"}), 400

    # Busca dados do CEP
    dados_cep = buscar_cep(cep)
    if "error" in dados_cep:
        return jsonify(dados_cep), 404

    # Busca dados adicionais
    codigo_ibge = dados_cep.get('ibge')
    dados_ibge = buscar_ibge(codigo_ibge)
    dados_ddd = buscar_ddd(dados_cep.get('ddd'))

    return jsonify({
        "cep": dados_cep,
        "ibge": dados_ibge,
        "ddd": dados_ddd
    })

if __name__ == '__main__':
    app.run(debug=True, port=5500)
