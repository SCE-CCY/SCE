from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/rules')
def rules():
    return render_template('rules.html')

@app.route('/roles')
def roles():
    return render_template('roles.html')

@app.route('/channels')
def channels():
    return render_template('channels.html')

@app.route('/essence')
def essence():
    return render_template('essence.html')

if __name__ == '__main__':
    # Считываем порт, который выдает Render, либо берем 5000 для локальных тестов
    port = int(os.environ.get("PORT", 5000))
    # Запуск на хосте 0.0.0.0 обязателен для работы в облаке
    app.run(host='0.0.0.0', port=port)
