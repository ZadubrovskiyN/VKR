#from crypt import methods
import flask
from flask import render_template
import pickle
import sklearn
from tensorflow import keras 
#import pandas as pd
from sklearn.linear_model import LinearRegression 
app = flask.Flask(__name__, template_folder = 'templates')
@app.route('/', methods = ['POST', 'GET'])
@app.route('/index', methods = ['POST', 'GET'])

def main():
    if flask.request.method == 'GET':
        return render_template('main.html')
    if flask.request.method == 'POST':
        with open('nn_model.pkl', 'rb') as f:
            loaded_model = pickle.load(f)
        
        module_uprugost = float(flask.request.form['module_uprugost'])
        soderjanie = float(flask.request.form['soderjanie'])
        pov_plotnost = float(flask.request.form['pov_plotnost'])
        prochn_rast = float(flask.request.form['prochn_rast'])
        ugol = float(flask.request.form['ugol'])
        plotn_nash = float(flask.request.form['plotn_nash'])
        plotnost = float(flask.request.form['plotnost'])
        kol_otv = float(flask.request.form['kol_otv'])
        temp = float(flask.request.form['temp'])
        module_rast = float(flask.request.form['module_rast'])
        potreb = float(flask.request.form['potreb'])
        shag = float(flask.request.form['shag'])
        
        y_pred = loaded_model.predict([[plotnost,module_uprugost,kol_otv,temp,pov_plotnost,module_rast,prochn_rast,potreb,ugol,shag,plotn_nash]])
        return render_template('main.html', result = y_pred)
      
if __name__ == '__main__':
    app.run()    