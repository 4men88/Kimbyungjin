from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = '문근영'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username




@app.route('/add')
def add():
    user = User()
    user.email='dddf@gmail.com'
    user.username='김바보'
    db.session.add(user)
    db.session.commit()
    return render_template('index.html')


@app.route('/insert')
def insert():
    ue = request.args.get('ue')
    uu = request.args.get('uu')
    user = User()
    user.email = ue
    user.username = uu
    db.session.add(user)
    db.session.commit()

    return render_template('index.html')


# @app.route('/')
# def index():
#     users= User().query.all()
#
#
#     return render_template('index.html', users= users)


# @app.route('/')
# def index():
#     a=[1,2,3,4,5,6,7,8,'a']
#     b=list('abcdefg')
#     c= list(zip(a,b))
#     print(c)
#     return render_template('index.html', users=c)




# @app.route('/')
# def index():
#
#     c= {'a':1,'b':2,'c':3,'d':4}
#     return render_template('index.html', users=c)



@app.route('/')
def index():

    users = User.query.all()
    return render_template('index.html', users=users)




@app.route('/search', methods=['post'])
def search():
    search_term = request.form['search']
    # search_term = request.form.get('search')

    if search_term =='study_1':
        return render_template('study_1.html')
    elif search_term =='study_2':
        return render_template('study_2.html')
    elif search_term =='study_3':
        return render_template('study_3.html')
    elif search_term =='study_4':
        return render_template('study_4.html')
    elif search_term =='study_5':
        return render_template('study_5.html')
    return redirect('/form')



if __name__ == '__main__':
    app.run()
