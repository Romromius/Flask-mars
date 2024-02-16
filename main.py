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
    params = {'title': "Главная"}
    return render_template('base.html', **params)


@app.route('/list_prof/<list>')
def list_prof(list: str):
    with open('worker manifest.txt', 'r', encoding='UTF-8') as f:
        worker_list = f.read().split('\n')
    params = {'title': 'Список персонала',
              'list': list,
              'workers': worker_list}
    return render_template('list_profs.html', **params)


@app.route('/training/<path>')
def training(path: str):
    param = {}
    param['title'] = "Кабинеты"
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
