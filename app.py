from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', log=None)

@app.route('/enviar', methods=['POST'])
def enviar():
    remetente = request.form['remetente']
    destinatario = request.form['destinatario']
    assunto = request.form['assunto']
    mensagem = request.form['mensagem']

    log = [
        "Iniciando conexão TCP com o servidor de e-mail (smtp.exemplo.com:25)...",
        ">> 220 smtp.exemplo.com Servidor SMTP pronto",
        f"<< HELO {remetente.split('@')[-1]}",
        ">> 250 smtp.exemplo.com Olá!",
        f"<< MAIL FROM:<{remetente}>",
        ">> 250 OK Remetente aceito",
        f"<< RCPT TO:<{destinatario}>",
        ">> 250 OK Destinatário aceito",
        "<< DATA",
        ">> 354 Inicie os dados da mensagem, termine com <CRLF>.<CRLF>",
        f"De: {remetente}",
        f"Para: {destinatario}",
        f"Assunto: {assunto}",
        "",
        mensagem,
        ".",
        ">> 250 OK Mensagem aceita para entrega",
        "<< QUIT",
        ">> 221 Conexão encerrada. Tchau!"
    ]

    return render_template('index.html', log=log)

if __name__ == '__main__':
    app.run(debug=True)
