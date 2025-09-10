import pickle
import json
import numpy as np
import Project_files.config as config


class EnergyConsumption():

    def __init__(self, Square_Footage, Number_of_Occupants, Appliances_Used,Average_Temperature, Day_of_Week, Building_Type):
        self.Square_Footage = Square_Footage
        self.Number_of_Occupants = Number_of_Occupants
        self.Appliances_Used = Appliances_Used
        self.Average_Temperature = Average_Temperature
        self.Day_of_Week = Day_of_Week
        self.Building_Type = 'Building_Type_' + Building_Type

    def load_model(self):
        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, 'r') as f:
            self.project_data = json.load(f)

    def get_predicted_EnergyConsumption(self):
        self.load_model()
       

        # test_array = np.zeros(self.model.n_features_in_)
        test_array = np.zeros(len(self.project_data['columns']))
        # print(len(self.project_data['columns']))
        test_array[0] = self.Square_Footage
        test_array[1] = self.Number_of_Occupants
        test_array[2] =  self.Appliances_Used
        test_array[3] = self.Average_Temperature
        test_array[4] = self.project_data['Day_of_Week'][self.Day_of_Week]
        energy_index = self.project_data['columns'].index(self.Building_Type)
        test_array[energy_index] = 1
        print('Test Array :', test_array)

        predicted_Consumption = self.model.predict([test_array])[0]
        # print(f'predicted Energy Consumption is: {round(predicted_Consumption,2)}')
        return predicted_Consumption

    
if __name__ == '__main__':
        Square_Footage = 24563
        Number_of_Occupants = 15
        Appliances_Used = 4
        Average_Temperature = 28.52
        Day_of_Week = 'Weekday'
        Building_Type = 'Residential'
        consumption = EnergyConsumption(Square_Footage, Number_of_Occupants, Appliances_Used,Average_Temperature, Day_of_Week, Building_Type)
        consumption.get_predicted_EnergyConsumption()

