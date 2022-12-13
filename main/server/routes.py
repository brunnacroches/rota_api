from flask import jsonify, request

from .server import app


# Esta é uma função para uma rota chamada "/rota1/acao1" usando o framework web Flask em Python. 
# A função retorna uma resposta JSON contendo informações sobre a rota e algum outro dado. 
# A função usa o método jsonify do Flask para converter o dicionário em um objeto JSON 
# e retorná-lo como resposta a uma requisição GET. 
# A função também retorna um código de status 200 para indicar que a solicitação foi bem-sucedida.
@app.route("/rota1/acao1", methods=["GET"])
def route_function():
    response = {
        "data": {
            "rota": "/rota1/acao1",
            "informacao": "Informação de acao1"
        }
    }
    return jsonify(response), 200

# Esta é uma função para uma rota chamada "/rota2/acao2" usando o framework web Flask em Python. 
# A função extrai os dados enviados no corpo da solicitação POST usando o método request.json 
# e armazena-os na variável body. Em seguida, a função cria uma resposta JSON c
# ontendo informações sobre a rota e o corpo da solicitação. 
# A função usa o método jsonify do Flask para converter o dicionário em um objeto JSON 
# e retorná-lo como resposta. A função também retorna um código de status 201 para 
# indicar que a solicitação foi bem-sucedida e que um novo recurso foi criado 
# como resultado da solicitação.
@app.route("/rota2/acao2", methods=["POST"])
def route_function2():
    body = request.json
    response = {
        "data": {
            "rota": "/rota2/acao2",
            "informação": "Informação ação 2",
            "body": body
        }
    }
    return jsonify(response), 201

# Esta é uma função para uma rota chamada "/rota3/acao3" usando o framework web Flask em Python. A função extrai os dados enviados no corpo da solicitação PATCH usando o método request.json e armazena-os na variável body. Em seguida, a função cria uma resposta JSON contendo informações sobre a rota e o corpo da solicitação. A função usa o método jsonify do Flask para converter o dicionário em um objeto JSON e retorná-lo como resposta. A função também retorna um código de status 201 para indicar que a solicitação foi bem-sucedida e que um novo recurso foi criado como resultado da solicitação.
# É importante observar que, embora a função retorne um código de status 201, ele não é o código 
# mais apropriado para uma solicitação PATCH. O código de status 201 é usado para indicar 
# que um novo recurso foi criado como resultado da solicitação. No caso de uma solicitação PATCH, 
# a intenção é atualizar um recurso existente, e não criar um novo. Portanto, o código de status
#  mais apropriado para uma solicitação PATCH é o 200 (OK) ou o 204 (Sem Conteúdo), dependendo da 
# necessidade.
@app.route("/rota3/acao3", methods=["PATCH"])
def route_function3():
    body = request.json
    response = {
        "data": {
            "rota": "/rota3/acao3",
            "informacao": "Informação de ação3",
            "body": body
        }
    }
    return jsonify(response), 201
