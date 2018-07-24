from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<name>')
@app.route('/')
def index(name=None):
    if name==None:
         return render_template('study1.html')
    elif name:
        return render_template('%s.html'%name)








#if __name__ == '__main__':
#    app.run(debug=True)
