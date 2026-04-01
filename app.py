from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Aula 4 – Testes com Pytest + Integração Completa com Git e GitHub Actions"



if __name__ == "__main__":
    app.run(debug=True, port=3000)