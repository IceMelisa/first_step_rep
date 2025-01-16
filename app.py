from flask import (
    Flask,
    render_template,
    request,
    redirect
)
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def get_home():
    # if request.method == 'POST':
    #     glass = 0
    #     soglass = 0
    #     age = request.form.get('age', type=str)
    #     for i in age:
    #         if i in 'aeyuio':
    #             glass += 1
    #         elif i in ' ':  
    #             print('Наггетс')
    #         else:
    #             soglass += 1

    #     return render_template('base.html', age=age, glass= glass, soglass=soglass)
        
    return render_template('base.html')

@app.route('/reg', methods=['GET','POST'])
def get_reg():

    return render_template('register.html')

@app.route('/log', methods=['GET','POST'])
def get_log():

    return render_template('login.html')



if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )