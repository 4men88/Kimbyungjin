from flask import Flask    #pep8 에 정의됨.

app = Flask(__name__)   #class의 instance화 & import module의 위치 호출


@app.route('/')     #@ == decorator  //함수의 동작을 동적으로 바꿔주는 애
def hello_world():
    return 'Hello World!'       #return == response


if __name__ == '__main__':
    app.run()

