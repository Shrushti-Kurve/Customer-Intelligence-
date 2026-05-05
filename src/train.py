import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier

# load data
df = pd.read_csv("../data/online_retail.csv", encoding="ISO-8859-1")

# basic cleaning
df = df.dropna()
df = df[df["Quantity"] > 0]

# feature
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# convert date
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# RFM
snapshot = df["InvoiceDate"].max()

rfm = df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (snapshot - x.max()).days,
    "InvoiceNo": "count",
    "TotalPrice": "sum"
})

rfm.columns = ["Recency", "Frequency", "Monetary"]

# scaling
scaler = StandardScaler()
scaled = scaler.fit_transform(rfm)

# clustering
kmeans = KMeans(n_clusters=4, random_state=42)
rfm["segment"] = kmeans.fit_predict(scaled)

# churn (simple logic)
rfm["churn"] = (rfm["Recency"] > 90).astype(int)

# model
X = rfm[["Recency", "Frequency", "Monetary"]]
y = rfm["churn"]

model = RandomForestClassifier()
model.fit(X, y)

# save
pickle.dump(model, open("../models/churn.pkl", "wb"))
pickle.dump(kmeans, open("../models/segment.pkl", "wb"))
pickle.dump(scaler, open("../models/scaler.pkl", "wb"))

print("Training complete and models saved")