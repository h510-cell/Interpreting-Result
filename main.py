import csv
import pandas as pd
import plotly_express as px
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv("filteringStars.csv")

mass = df["Mass"].tolist()
radius = df["Radius"].tolist()
star_name = df["Star_name"].tolist()
distance = df["Distance"].tolist()
gravity = df["Gravity"]

fig = px.bar(x = star_name, y = mass)
fig.show()

fig = px.bar(x = star_name, y = radius)
fig.show()

fig = px.bar(x = star_name, y = distance)
fig.show()

fig = px.bar(x = star_name,y = gravity)
fig.show()

