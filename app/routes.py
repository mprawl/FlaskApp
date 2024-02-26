from app import app
from flask import render_template, flash, redirect, request, url_for, jsonify
from app.forms import LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            flash('Welcome user {}! You opted for remember_me={}'.format(
                form.username.data, form.remember_me.data))
            return redirect(url_for('mprawl'))
        else:
            if request.args:
                flash('GET method now allowed for login!')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/mprawl')
#a view function – route handler
def mprawl():
    return render_template('mprawl.html') 


#routes – URLs where a flask app accepts requests
@app.route('/')
@app.route('/index')
#a view function – route handler
def index():
    user = {'username': 'mprawl'}
    classes = [{'classInfo': {'code': 'CSC324', 'title': 'DevOps'}, 'instructor': 'Baoqiang Yan'},
        {'classInfo': {'code': 'CSC184', 'title': 'Python Programming'}, 'instructor': 'Evan Noynaert'}]
    return render_template('index.html', title='Home', user=user, classes=classes) 


@app.route('/json')
def jsonTest():
    # return jsonify(list(range(5)))
    instructor = {"username": "mprawl",
                  "role": "student",
                  "uid": 11,
                  "name":
                      {"firstname": "Megan",
                       "lastname": "Prawl"
                       }
                  }

    return jsonify(instructor)


@app.route('/restlogin', methods=['GET', 'POST'])
def loginAPI():
    json_data = request.get_json(force = True)
    if json_data:
        username = json_data["username"]
        password = json_data["password"]
    else:
        return '{"Success":false}'
    if username == 'mprawl' and password == '123':
        return '{"Success":true}'
    return '{"Success":false}'