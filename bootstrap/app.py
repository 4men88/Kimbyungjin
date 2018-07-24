from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config.update({'SECRET_KEY':'문근영'})#내맘대로 암호규칙...?;;

class MyForm(FlaskForm):
    text = StringField('text1', validators=[DataRequired()])
    password = PasswordField('password1', validators=[DataRequired()])


class SearchForm(FlaskForm):
    search = StringField("검색", validators=[DataRequired()])

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/search', method=['post'])
def search():
    return render_template('search.html')





@app.route('/form', methods=['GET','POST'])
def form():
    form = MyForm()
    if request.method=='GET':
        if form.validate_on_submit():
            return render_template('index.html')
                 #a= request.args.get('a','')    #get을 쓰면 '' default 값을 줄 수 있다.
                 #b= request.args['a']          #dictionary type과 똑같은 방법으로 indexing 가능
                 #c= request.args.a             #?? pandas???


                 #print(a)
                 #print(b)
                 #print(c)
        return render_template('form.html', form2=form)
    else:
        return render_template('form.html', form2=form)

#    a = request.form('moon')
#   b = request.args
#  print(a)
# print(b)
#     return render_template('form.html')






#if __name__ == '__main__':
#    app.run(debug = True)

