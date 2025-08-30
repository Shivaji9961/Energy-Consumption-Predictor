
from flask import Flask, jsonify, request, render_template
import pandas as pd
import numpy as np
import joblib
import os
import Project_files.config as config
from Project_files.utils import EnergyConsumption

app = Flask(__name__)

 
@app.route('/')
def home():
    return render_template('index.html')




@app.route('/predict_charges', methods = ['GET', 'POST'])
def get_Energy_Consumption():
    if request.method =='POST':
        print('We are in POST Method')
        data = request.form
        Square_Footage = data['Square_Footage']
        Number_of_Occupants = data['Number_of_Occupants']
        Appliances_Used = data['Appliances_Used']
        Average_Temperature = eval(data['Average_Temperature'])
        Day_of_Week = data['Day_of_Week']
        Building_Type = data['Building_Type']
       
        consumption =EnergyConsumption(Square_Footage, Number_of_Occupants, Appliances_Used,Average_Temperature, Day_of_Week, Building_Type)
        Charges = consumption.get_predicted_EnergyConsumption()
        return jsonify({'Result': f' Energy Consumption : {round(Charges,2)}'})
    
    else:
        print('We are in GET Method')
        data1 = request.form
        Square_Footage = data1['Square_Footage']
        Number_of_Occupants = data1['Number_of_Occupants']
        Appliances_Used = data1['Appliances_Used']
        Average_Temperature = data1['Average_Temperature']
        Day_of_Week = data1['Day_of_Week']
        Building_Type = data1['Building_Type']
        
        consumption1 =EnergyConsumption(Square_Footage, Number_of_Occupants, Appliances_Used,Average_Temperature, Day_of_Week, Building_Type)
        Charges = consumption1.get_predicted_EnergyConsumption()
        return jsonify({'Result': f'Energy Consumption  : {round(Charges,2)}'})
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= config.PORT_NUMBER, debug=True)