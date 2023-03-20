from flask import Flask, render_template, json, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)



@app.route('/')
@app.route('/index/<name>')
def index(name):
    title = name
    return render_template('index.html', title=title)

@app.route('/odd_even')
def odd_even():
    return render_template('if_file.html', number=5)

@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('for_file.html')


@app.route('/training/<prof>')
def prof(prof):
    return render_template('prof.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')