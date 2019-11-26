from flask import Flask

app = Flask(__name__)

@app.route('/')
def index_page_landing():
    return '<h1>Welcome</h1>'

@app.route('/secondpage')
def secondpage():
    return '<h2>prova seconda pagina</h2>'


if __name__ == "__main__":
    app.run()
