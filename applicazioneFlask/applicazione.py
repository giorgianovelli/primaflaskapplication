from flask import Flask, request, render_template

app = Flask(__name__)

#Mapping URL multipli
@app.route('/')
@app.route("/<user>")
def index(user=None):
     return render_template("user.html", user=user)

#Passaggio obj nei templates
@app.route("/shopping")
def shopping():
    food=["cheese", "tuna", "beef", "toothpaste"]
    return render_template("shopping.html", food=food)

#restituisce il metodo usato (get o post)
# @app.route('/')
# def index_page_landing():
#      return "Method used: %s" %request.method

#controlla quale metodo viene usato
@app.route("/provametodi", methods=['GET', 'POST'])
def provametodi():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are using GET"

@app.route('/secondpage')
def secondpage():
    return '<h2>prova seconda pagina</h2>'

#passaggio variabile inserita nell'URL al file html
@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)

#passaggio variabile numerica nell'URL alla stringa in output
@app.route('/post/<int:post_id>')
def post(post_id):
    return "Post id is %s" % post_id


if __name__ == "__main__":
    app.run()
