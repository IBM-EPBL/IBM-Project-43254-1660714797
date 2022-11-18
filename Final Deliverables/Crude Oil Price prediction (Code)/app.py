import numpy as np  # used for numerical analysis
from flask import Flask, render_template, request, url_for, redirect  # Flask is a application used to run/serve our application
# request is used to access the file which is uploaded by the user in our application
# render_template is used for rendering the html pages
from tensorflow.keras.models import load_model  # we are loading our model from keras


app = Flask(__name__)  # our flask app
model = load_model('crude_oil_price_prediction.h5')  # loading the model in the flask app

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        if request.form['username'] != "PNT2022TMID43400" or request.form['password'] != "7155":
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('mains'))
    return render_template('login.html', error=error)


@app.route('/mains', methods=['GET', 'POST'])
def mains():
    return render_template('index.html')

@app.route('/stats', methods=['GET', 'POST'])
def stats():
    return render_template('stats.html')



@app.route('/about')
def home1():
    return render_template("index.html")  # rendering html template


@app.route('/predict')
def home2():
    return render_template("web.html")  # rendering html template

@app.route('/contact')
def contact():
    return render_template("contact.html") 


@app.route('/login', methods=['POST'])  # route for our prediction
def login():
    a = request.form['year1']
    b = request.form['year2']
    c = request.form['year3']
    d = request.form['year4']
    e = request.form['year5']
    f = request.form['year6']
    g = request.form['year7']
    h = request.form['year8']
    i = request.form['year9']
    j = request.form['year10']  # requesting the file
    x_input = [[float(a), float(b), float(c), float(d), float(e), float(f), float(g), float(h), float(i), float(j)]]
    print(x_input)
    lst_output = model.predict(x_input)
    lst_output = np.round(lst_output[0][0], 2)
    return render_template("web.html", showcase='The Predicted crude oil price is : Rs. '+str(lst_output))


if __name__ == '__main__':
    app.run(debug=False)