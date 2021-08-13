import flask
import pandas as pd
import pickle
import sklearn.preprocessing._label
from flask import Flask,render_template, request, redirect, url_for

app = Flask(__name__)
## loading the model
pickle_in = open('xgcars.pkl','rb')
predictor = pickle.load(pickle_in)

## loading the model for premium cars(merc, bmw and audi)
prem_pickle_in = open('premXgrmodel.pkl','rb')
prem_predictor = pickle.load(prem_pickle_in)

## loading the make encoder
make_pickle_in = open('make.pkl','rb')
make_transformer = pickle.load(make_pickle_in)

## loading the make encoder for premium cars
premMake_pickle_in = open('premMake.pkl','rb')
premMake_transformer = pickle.load(premMake_pickle_in)

## loading the model encoder
model_pickle_in = open('model.pkl','rb')
model_transformer = pickle.load(model_pickle_in)

## loading the model encoder for premium cars
premModel_pickle_in = open('premModel.pkl','rb')
premModel_transformer = pickle.load(premModel_pickle_in) 


## loading the fuel encoder
fuel_pickle_in = open('fuel.pkl','rb')
fuel_transformer = pickle.load(fuel_pickle_in)

## loading fuel encoder for premium cars

premFuel_pickle_in = open('premFuel.pkl', 'rb')
premFuel_transformer = pickle.load(premFuel_pickle_in)

## loading the transmission encoder
trans_pickle_in = open('trans.pkl','rb')
trans_transformer = pickle.load(trans_pickle_in)

## loading the transmission encoder for premium cars



@app.route('/')
def hello():
    return 'welcome!'

@app.route('/predict', methods = ["GET","POST"])
def predict_price():
    if request.method == "POST":
        web_make = request.form['make'].lower()
        
    
        mke = int(make_transformer.transform([web_make])[0])

        web_model = request.form['model']
        mdel = int(model_transformer.transform([web_model])[0])

        yr = int(request.form['year'])

        web_trans = request.form['transmission']
        trans = int(trans_transformer.transform([web_trans])[0])

        miles = int(request.form['mileage'])

        web_fuel = request.form['fuel']
        fuel = int(fuel_transformer.transform([web_fuel])[0])

        engine=float(request.form['enginesize'])

        tx = float(request.form['tax'])

        mpgal = float(request.form['mpg'])

        data = {'year':yr,'transmission':1,'mileage':miles,'fuelType':fuel,'tax':tx,
                               'mpg':mpgal,'engineSize':engine,'make':mke,'model':mdel}
        test_df = pd.DataFrame(data,index=[0])
        predicted_price = round(float(predictor.predict(test_df)[0]),2)
        error_price = predicted_price*2.04/100
        min_price = round((predicted_price - error_price),2)
        max_price = round((predicted_price + error_price),2)
        ##return '<h1>The predicted price is {{ predicted_price }} </h1>'
        return render_template('result.html', prediction=str(predicted_price), min_price=str(min_price),max_price=str(max_price))

    
    ##return render_template('index.html', prediction=str(predicted_price))"""
    #print(tx)
    #return render_template('result.html',predicted_price=tx)
    
    ##return "the predicted car price is " + str(predicted_price)
    else:
        return render_template('index.html')

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