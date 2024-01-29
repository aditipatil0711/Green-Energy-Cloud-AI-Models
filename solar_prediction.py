from flask import Flask, request, jsonify, render_template
from sklearn.preprocessing import StandardScaler
import flask_cors
import pandas as pd

filename_rf = 'C:\\Users\\patil\\Green_Cloud\\ML-Backend-Solar\\rf_random_stddata_model.pkl'
filename_2step_rf = 'C:\\Users\\patil\\Green_Cloud\\ML-Backend-Solar\\Pickle_TwoStep_rf_Model.pkl'
filename_2step_svr = 'C:\\Users\\patil\\Green_Cloud\\ML-Backend-Solar\\Pickle_TwoStep_SVR_Model.pkl'
weekly_average_rf = pd.read_csv('C:\\Users\\patil\\Green_Cloud\\ML-Backend-Solar\\test_df_daily.csv')
weekly_average_2step = pd.read_csv('C:\\Users\\patil\\Green_Cloud\\ML-Backend-Solar\\test_df_daily.csv')
train_stdf0 = pd.read_csv('C:\\Users\\patil\\Green_Cloud\\ML-Backend-Solar\\train_stdf.csv')
y_train_svr = train_stdf0['output']
y_train_svr=y_train_svr.to_numpy()
y_train_svr = y_train_svr.reshape(-1,1)
sc_y = StandardScaler()
y = sc_y.fit_transform(y_train_svr)

app = Flask(__name__)
flask_cors.CORS(app)

purpose3 = 'Get Predictions of test data'
purpose4 = 'Get predictions with data input'

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # Assuming your prediction logic and data are here
    # For example:
    def calculate_weekly_average():
        # Define the logic to calculate the weekly average
        print("calculate_weekly_average")
        pass

    weekly_average_rf = calculate_weekly_average() # Replace with actual function
    r2_hourly = 0.91  # Coefficient of Determination R^2 for Hourly predictions
    r2_weekly = 0.90  # Coefficient of Determination R^2 for Weekly average

    response = {
        "weekly_average": weekly_average_rf,
        "performance_metrics": {
            "solar_hourly": r2_hourly,
            "solar_weekly": r2_weekly
        }
    }

    print(response)
    return jsonify(response)

@app.route('/predict2', methods=['GET', 'POST'])
def predict2():
    # Assuming your prediction logic and data are here
    # For example:
    def calculate_weekly_average():
        # Define the logic to calculate the weekly average
        print("calculate_weekly_average")
        pass

    weekly_average_rf = calculate_weekly_average() # Replace with actual function
    r2_hourly = 0.84  # Coefficient of Determination R^2 for Hourly predictions
    r2_weekly = 0.92  # Coefficient of Determination R^2 for Weekly average

    response = {
        "weekly_average": weekly_average_rf,
        "performance_metrics": {
            "r2_hourly": r2_hourly,
            "r2_weekly": r2_weekly
        }
    }

    print(response)
    return jsonify(response)

if __name__ == '__main__':
    print(purpose3)
    app.run(debug=True)

   