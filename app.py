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
        "S: 220 smtp.exemplo.com ESMTP Postfix (Servidor pronto para conexão)",
        f"C: HELO {remetente.split('@')[-1]}",
        "S: 250 smtp.exemplo.com Olá cliente, conexão estabelecida",
        f"C: MAIL FROM:<{remetente}>",
        "S: 250 2.1.0 OK - Remetente aceito",
        f"C: RCPT TO:<{destinatario}>",
        "S: 250 2.1.5 OK - Destinatário aceito",
        "C: DATA",
        "S: 354 Inicie os dados da mensagem; termine com <CRLF>.<CRLF>",
        f"C: De: {remetente}",
        f"C: Para: {destinatario}",
        f"C: Assunto: {assunto}",
        "C:",
        f"C: {mensagem}",
        "C: .",
        "S: 250 2.0.0 OK - Mensagem aceita e enfileirada para entrega (ID: 12345)",
        "C: VRFY destinatario",
        "S: 252 Não é possível verificar o usuário, mas a mensagem será entregue",
        "C: NOOP",
        "S: 250 OK - Conexão ativa",
        "C: RSET",
        "S: 250 2.0.0 Estado da transação redefinido",
        "C: QUIT",
        "S: 221 smtp.exemplo.com Conexão encerrada. Tchau!",
        "",
        "📘 Explicação dos principais comandos:",
        "- HELO: inicia a comunicação e identifica o cliente.",
        "- MAIL FROM: define o endereço do remetente.",
        "- RCPT TO: define o(s) destinatário(s).",
        "- DATA: envia cabeçalhos e corpo da mensagem; termina com um ponto (.).",
        "- VRFY: tenta verificar um usuário (geralmente desabilitado).",
        "- NOOP: checa se o servidor está respondendo.",
        "- RSET: limpa o estado da sessão atual sem fechar.",
        "- QUIT: encerra a sessão SMTP com segurança."
    ]

    return render_template('index.html', log=log)

if __name__ == '__main__':
    app.run(debug=True)
