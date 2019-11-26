from flask import Flask, request, render_template

app = Flask(__name__)

# @app.route('/')
# def index_page_landing():
#     return '<h1>Welcome</h1>'

@app.route('/')
def index_page_landing():
     return "Method used: %s" %request.method

@app.route("/provametodi", methods=['GET', 'POST'])
def provametodi():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are using GET"

@app.route('/secondpage')
def secondpage():
    return '<h2>prova seconda pagina</h2>'

@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)

@app.route('/post/<int:post_id>')
def post(post_id):
    return "Post id is %s" % post_id


if __name__ == "__main__":
    app.run()
