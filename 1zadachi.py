from flask import Flask, url_for, request

app = Flask(__name__)

lst = [
    'Человечество вырастает из детства.',
    'Человечеству мала одна планета.',
    'Мы сделаем обитаемыми безжизненные пока планеты.',
    'И начнем с Марса!',
    'Присоединяйся!'
]


@app.route('/')
def general():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '</br></br>'.join(lst)

@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                  <h1>Жди нас, Марс!</h1>
                  <img src="/static/img/mars.jpg" alt="здесь должна была быть картинка, но не нашлась">
                    <p>Вот она какая красная планета<p>
                  </body>
                </html>"""



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
