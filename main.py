from flask import Flask, render_template

app = Flask(__name__) # переменная "name" содержит имя текущего модуля, содержит в себе имя текущего модуля, помогает фреймворку находить ресурсы(папки и прочее)

@app.route('/') # этот декоратор используется для присвоения URL адреса функциям
def hello_world():
    return render_template('index.html')

@app.route('/person/')
def person():
    return render_template('main.html')

if __name__ == '__main__': # проверяем запущен ли скрипт и запускаем локальный сервер
    app.run()