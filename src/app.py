from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    todolist=[{
        'id':1,
        'text':'teach flask',
        'completed':False
    },{
        'id':2,
        'text':'teach Python',
        'completed':True
    }
    ]
    return render_template('index.html',data=todolist)

@app.route('/about')
def about():
    return 'About Page'

@app.route('/contact')
def contact():
    return 'contact Page'

if __name__ == '__main__':
    app.run(debug=True)