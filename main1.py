from flask import Flask, render_template

app = Flask(__name__) # переменная "name" содержит имя текущего модуля, помогает фреймворку находить ресурсы(папки и прочее)

@app.route('/') # этот декоратор используется для присвоения URL адреса функциям
def hello_world():
    context = {
        "caption": "Большой куш",
        "link": "Посмотреть про актёра"
    }
    return render_template('index1.html', **context)

@app.route("/shablon/")
def hello_world2():
    context = {
        "caption": "Фильм Большой куш",
        "link": "Посмотреть на кинопоиск"
    }
    return render_template('index1.html', **context)

@app.route('/person/')
def person():
    return render_template('main.html')

if __name__ == '__main__': # проверяем запущен ли скрипт и запускаем локальный сервер
    app.run()