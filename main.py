from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user
from flask_restful import Api

# import mars_api
import user_resources
from data import db_session
from data.users import User
from forms.user import RegisterForm, LoginForm

app = Flask(__name__)
api = Api(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'glory to NSSA'


def figurates(phrase: str, words: type([]) | set):
    """
    Определяет, фигурирует ли какая-либо строка из списка в другой строке.

    Аргументы:
        phrase: строка, которую предстоит анализировать.
        words: список или множество слов, которые будут искаться в строке.

    Возвращает:
        True или False, в зависимости от того, найдена ли хоть какая-либо строка в phrase.
    """
    for i in words:
        if i in phrase:
            return True
    return False


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        print(user.name)
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


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
    api.add_resource(user_resources.UserListResource, '/api/v2/users')
    api.add_resource(user_resources.UsersResource, '/api/v2/users/<int:user_id>')
    db_session.global_init("db/mars_explorer.db")
    # app.register_blueprint(mars_api.blueprint)
    app.run(port='8080', host='127.0.0.1')
