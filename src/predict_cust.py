import joblib as job
import pandas as pd

#Load Model and Scaler
model = job.load("../model/customer_seg_model.pkl")
scaler = job.load("../model/scaler.pkl")

#Input data
Income = float(input("Enter the Income from Customer:"))
SpendingScore = float(input("Enter the Spending Score of Customer:"))

new_df = pd.DataFrame([[Income,SpendingScore]],columns = ["AnnualIncome","SpendingScore"])

#Scale input
scaled_data = scaler.transform(new_df)

#Predict Cluster
cluster = model.predict(scaled_data)[0]

if cluster == 0:
    print("Low income , High spending Customer.")
elif cluster == 1:
    print("High income, Low spending Customer.")
elif cluster == 2:
    print("Low income, Low spending Customer.")
elif cluster == 3:
    print("Medium income, Medium spending Customer.")
elif cluster == 4:
    print("High income, High spending Customer.")