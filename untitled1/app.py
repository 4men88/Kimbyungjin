from flask import Flask,render_template            #flask 는 주소를 받아 결과값을 제공한다.

app = Flask(__name__)


@app.route('/')      #내 주소에 아무것도 입력하지 않았을 때 : /, && 주소값을 이용하여 output보여주는
def hello_world():
     #todo 나 열심히 할게요
    return '<h1>Hello World!</h1>'       #html tag 사용 가능 but 사용 안함.


@app.route('/a')
def hello_world2():
    #todo 나 열심히 할게요
    return 'Hello World2!'


@app.route('/a/b')
def hello_world3():
    #todo 나 열심히 할게요
    return 'Hello World3!'

@app.route('/x')
def hello_world5():
    #todo 나 열심히 할게요
    return render_template('decorator.html')



@app.route('/c/<name>')
def hello_name():
    #todo 나 열심히 할게요
    return '<h1>%s</h1>' % name




if __name__ == '__main__':
    app.run(debug=True)

#사용자 input 값 결정 && 서버 output 값 결정  (주소값 || link || form 입력)