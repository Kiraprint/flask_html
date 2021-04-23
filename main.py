from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/<title>')
def base(title):
    return render_template('base.html', title=title, css=url_for('static', filename='css/style.css'))


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof, img=url_for('static', filename='img/scheme.png'))

@app.route('/answer')
@app.route('/answer_auto')
def answer():
    params = {'title': 'Анкета', 'surname': 'Watny', 'name': 'Mark', 'education': 'выше среднего',
              'profession': 'штурман марсохода', 'sex': 'male', 'motivation': 'Всегда мечтал застрять на Марсе!',
              'ready': True}
    return render_template('auto_answer.html', **params)

@app.route('/list_prof/<key>')
def list_prof(key):
    profs = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог',
             'врач', 'инженер по терраформированию',
             'климатолог', 'специалист по радиационной защите',
             'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения',
             'метеоролог', 'оператор марсохода', 'киберинженер',
             'штурман', 'пилот дронов']
    return render_template('list_prof.html', key=key, profs=profs)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
