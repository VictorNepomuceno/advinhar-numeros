from flask import Flask, render_template, request
import random 

app = Flask(__name__, template_folder="template")

@app.route("/")
def index():
    return render_template("main.html")


@app.route("/jogo", methods=["POST"])
def jogo():
    numeroSecreto = random.randint(1, 100)

    tentativas = 0

    while True:     
        palpite = int(request.form["numero"])

        tentativas += 1

        if palpite == numeroSecreto:
            mensagem = f"Parabéns, voce acertou em {tentativas} tentativas!!"
            return render_template('resultado.html', mensagem=mensagem)
        
        elif palpite < numeroSecreto / 2:
            mensagem = "Baixo demaissss, tenta novamente po"

        elif palpite < numeroSecreto:
            mensagem = "Ta chegando perto, mas ainda está baixo, tente novamente"
        
        elif palpite < numeroSecreto - 10:
            mensagem = "Ta muito perto, tenta denovo que voce consegue!"

        elif palpite > numeroSecreto * 2:
            mensagem = "Muito longeee, tenta novamente po"

        elif palpite > numeroSecreto + 10:
           mensagem = "Ta chegando perto, mas está alto,  tenta denovo que voce consegue!"
        
        else:
            mensagem = "Ta muito perto, tenta denovo que voce consegue!"

        return render_template('main.html', mensagem=mensagem)
    
if __name__ == '__main__':
    app.run(debug=True)
    

   






