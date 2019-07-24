from flask import Flask, render_template, url_for, request

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
    locationdata ={
        'bangalore':'karnataka',
         'mumbai':'Maharashtra'
    }
    location = request.args.get('location')
    state = locationdata[location]
    return render_template('index.html',todolist=todolist, state=state)

@app.route('/about')
def about():
    return 'About Page'

@app.route('/contact')
def contact():
    return 'contact Page'

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        locationdata ={
            'bangalore':'karnataka',
            'mumbai':'Maharashtra'
            }
        location = request.form.get('location')
        state = locationdata[location]
        return render_template('form.html', state=state)
    else:
        return render_template('form.html', state='..')


if __name__ == '__main__':
    app.run(debug=True)