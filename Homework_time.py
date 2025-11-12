from flask import Flask, render_template
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

@app.route('/')
def time():
    now = datetime.now(ZoneInfo('Europe/Moscow'))
    formatted = now.strftime('%Y-%m-%d %H:%M:%S')
    return render_template('Homework_time.html', now=now, formatted=formatted)

if __name__ == '__main__':
    app.run(debug=True)