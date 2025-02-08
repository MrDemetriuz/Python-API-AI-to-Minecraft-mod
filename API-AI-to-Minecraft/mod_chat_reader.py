import threading
import requests 
import time
from flask import Flask, jsonify, request

app = Flask(__name__)

def format_chat():
    duplicated_list = []
    while True:
        with open("e:/chat_messages.txt", "r", encoding="utf-8") as chat:
            conteudo = chat.read()

            inicio = conteudo.rfind('<MrDemiurgo>')
            fim = len(conteudo)

            chat_formated = conteudo[inicio:fim]
            if chat_formated not in duplicated_list:
                print(chat_formated)
                duplicated_list.append(chat_formated)
                post_text_to_ai(chat_formated)
            else:
                time.sleep(10)

@app.route('/textToAi', methods=['POST'])
def post_text_to_ai(chat_formated):
    # Ajustando o envio de dados JSON corretamente
    url_api = "http://localhost:5001/api/v1/generate"
    post_chat = {'prompt': chat_formated}

    resposta = requests.post(url_api, json=post_chat)

    #return jsonify({'status': resposta.status_code, 'resposta': resposta.json()})

def main():
    # Usando threading para rodar format_chat simultaneamente
    thread = threading.Thread(target=format_chat)
    thread.start()

    app.run()

if __name__ == '__main__':
    main()

