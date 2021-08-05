import flask
import pandas as pd
import pickle
import sklearn.preprocessing._label
from flask import Flask,render_template, request

app = Flask(__name__)
## loading the model
pickle_in = open('xgcars.pkl','rb')
predictor = pickle.load(pickle_in)

## loading the make encoder
make_pickle_in = open('make.pkl','rb')
make_transformer = pickle.load(make_pickle_in)

## loading the make encoder
model_pickle_in = open('model.pkl','rb')
model_transformer = pickle.load(model_pickle_in)

## loading the fuel encoder
fuel_pickle_in = open('fuel.pkl','rb')
fuel_transformer = pickle.load(fuel_pickle_in)

## loading the transmission encoder
trans_pickle_in = open('trans.pkl','rb')
trans_transformer = pickle.load(trans_pickle_in)

@app.route('/')
def hello():
    return 'welcome!'

@app.route('/predict', methods = ['POST'])
def predict_price():
    web_make = request.form['make']
    mke = int(make_transformer.transform([web_make])[0])

    web_model = request.form['model']
    mdel = int(model_transformer.transform([web_model])[0])

    yr = int(request.form['year'])

    web_trans = request.form['transmission']
    trans = int(trans_transformer.transform([web_trans])[0])

    miles = int(request.form['mileage'])

    web_fuel = request.form['fuel']
    fuel = int(fuel_transformer.transform([web_fuel])[0])

    engine=float(request.form['engineSize'])

    tx = float(request.form['tax'])

    mpgal = float(request.form['mpg'])

    data = {'year':yr,'transmission':1,'mileage':miles,'fuelType':fuel,'tax':tx,
                               'mpg':mpgal,'engineSize':engine,'make':mke,'model':mdel}
    test_df = pd.DataFrame(data,index=[0])
    predicted_price = predictor.predict(test_df)[0]
    return "the predicted car price is " + str(predicted_price)

@app.route('/content')
def content():
    return 'The content page for the application - first flast app code'

@app.route('/aboutpage')
def about():
    return 'about page content'

@app.route('/htmpage1')
def htmpage1():
    return '<h1>This is the firt html output line from a python app</h1>'

@app.route('/index')
def index():
    return render_template('index.html')
        


if __name__=='__main__':
    app.run(debug = True)