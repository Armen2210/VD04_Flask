from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_homework_VD05_Jinja.html', active_page='home')

@app.route('/blog')
def blog():
    return render_template('blog_homework_VD05_Jinja.html', active_page='blog')

@app.route('/contacts')
def contacts():
    return render_template('contacts_homework_VD05_Jinja.html', active_page='contacts')

if __name__ == '__main__':
    app.run(debug=True)
