from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Aula 3 – Arquitetura da Integração Contínua e GitHub Actions 🚀"

if __name__ == "__main__":
    app.run(debug=True, port=3000)