import json
import random

from flask import Flask, render_template, redirect, request

from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    param = {}
    param['title'] = title
    return render_template('base.html', **param)


@app.route('/training/', defaults={"prof": ""})
@app.route('/training/<prof>')
def training(prof):
    param = {}
    param['prof'] = prof.lower()
    return render_template('training.html', **param)


@app.route('/list_prof/', defaults={"list": "ul"})
@app.route('/list_prof/<list>')
def list_prof(list):
    param = {}
    param["professions"] = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                            'инженер по терраформированию', 'климатолог',
                            'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                            'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                            'штурман', 'пилот дронов']
    param['list'] = list
    return render_template('list_prof.html', **param)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    param = {"title": "Анкета",
             "surname": "Watny",
             "name": "Mark",
             "education": "выше среднего",
             "profession": "штурман марсохода",
             "sex": "male",
             "motivation": "Всегда мечтал остаться на Марсе!",
             "ready": "True"}
    return render_template('auto_answer.html', **param)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/distribution')
def distribution():
    list_members = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('distribution.html', members=list_members)


@app.route('/table/<sex>/<int:number>')
def table(sex, number):
    return render_template('table.html', sex=sex, number=number)


@app.route('/member')
def member():
    with open('templates/membres.json', encoding='utf-8') as f:
        data = json.load(f)
    return render_template('members.html', list=data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
