import pandas as pd
import numpy as np

class hlthCalculator():

    def assign_health_risk(df):
        if df is not None:
            if "BMI" in df.columns:  ## check if this column exists in the dataFrame
                df["Health risk"] = np.where(  ## Create derived column that will hold the Health risk indicator
                     (df["BMI"] >= 18.4), 'Malnutrition risk',
                    np.where(
                     (df["BMI"] >= 18.5) & (df["BMI"] <= 24.9), 'Low risk',
                    np.where(
                     (df["BMI"] >= 25) & (df["BMI"] <= 29.9), 'Enhanced risk',
                    np.where(
                     (df["BMI"] >= 30) & (df["BMI"] <= 34.9), 'Medium risk',
                    np.where(
                     (df["BMI"] >= 35) & (df["BMI"] <= 39.9), 'High risk',
                    np.where((df["BMI"] >= 40), 'Very high risk', 'not in threshold'))))))
                df["Count_of_overwight"] = len(
                    df[
                        (df["BMI"] >= 25) &
                        (df["BMI"] <= 29.9)
                        ]
                )
                return df
            else:
                return "BMI not processed yet"
        else:
            return ''

    def calculate_BMI(data):
        if len(data) >0:  ##Validating the input list of dictionary objects
            df = pd.DataFrame(data)
            df["BMI"] = round((df["HeightCm"] / (df["WeightKg"] * df["WeightKg"])) * 100, 2)
            return df
        else:
            print("Health risk data not supplied. BMI could not be calculated. Contact the data supplier. Thanks.")

    def return_data():
        data = [
                {"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
                { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
                { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
                { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
                {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
                {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
               ]
        return data

if __name__ == '__main__':
    ## Get BMI value for each person
    Bmi_df = hlthCalculator.calculate_BMI(hlthCalculator.return_data())
    ##Check health risk status
    health_risk_df = hlthCalculator.assign_health_risk(Bmi_df)
    print(health_risk_df)  ###Only for debuging

    # save result set to local marchine

    file_name = 'HeartRisk_processed.csv'
    #path = 'C:\\Users\\Begho\\CalculatorProject\\'+file_name
    #health_risk_df.to_csv(path)
    print('')
    print('file processed')

    ##Clean up
    del Bmi_df
    del health_risk_df
