from flask import Flask, render_template, request
from responde import Responder
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api_ghost', methods=['POST'])
def receberdados():
    try:
       txt= Responder.responder_chat(request.form['msg'])
       return txt.replace("```","<code>").replace("```", "</code>")
    except:
        return " Descupa ocorreu um erro interno, Envie um feedback para a nossa equipe 😭💔"