from flask import Flask, render_template, request

app = Flask(__name__)


def figurates(phrase: str, words: list | set):
    """
    Определяет, фигурирует ли какая-либо строка из списка в другой строке

    Аргс:
        phrase: строка, которую предстоит анализировать
        words: список или множество слов, которые будут искаться в строке

    Возвращает:
        True или False, в зависимости от того, найдена ли хоть какая-либо строка в phrase
    """
    for i in words:
        if i in phrase:
            return True
    return False


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['title'] = "Главная"
    return render_template('base.html', **param)


@app.route('/training/<path>')
def training(path: str):
    param = {}
    param['title'] = "Главная"
    deck = 'Палуба не определена 🤖'

    if figurates(path.lower(), ['лог', 'атр', 'евт']):
        deck = 'Лазарет'
        param['image'] = '/static/img/morg.png'
    if figurates(path.lower(), ['ург', 'пат']):
        deck = 'Операционная'
        param['image'] = '/static/img/operational.png'  # Надо без повторов
    param['train_site'] = deck
    return render_template('training.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
