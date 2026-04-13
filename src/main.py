import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import joblib as job

#load data
df = pd.read_csv("../data/customers.csv")

#Select features
x = df[["AnnualIncome","SpendingScore"]]

#Scaling
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

#Elbow Method
wcss = []

for i in range(1 , 11):
    kmeans = KMeans(n_clusters = i, random_state = 42)
    kmeans.fit(x_scaled)
    wcss.append(kmeans.inertia_)

#Plot Elbow Graph
plt.plot(range(1,11),wcss)
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

#Apply KMeans (Choose 5 clusters)
kmeans = KMeans(n_clusters = 5,random_state = 42)
y_means = kmeans.fit_predict(x_scaled)

#Plot Clusters
plt.scatter(x["AnnualIncome"], x["SpendingScore"], c = y_means)

#Add Centroids
centroids = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(centroids[:,0],
            centroids[:,1],
            s = 200, c = 'red', marker = 'x')

plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()

#Save the Output
df["Clusters"] = y_means
df.to_csv("../data/output.csv", index = False) 

#Save Model and scaler
job.dump(kmeans,"../model/customer_seg_model.pkl")
job.dump(scaler,"../model/scaler.pkl")

print(df.groupby("Clusters").mean())