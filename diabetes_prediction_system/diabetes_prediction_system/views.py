from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
def home(request):
    return render (request,'home.html')
def predict(request):
    return render (request,'predict.html')
def result(request):
    data = pd.read_csv(r"c:\Users\PC\Downloads\diabetes.csv")
    X = data.drop("Outcome", axis=1)
    y = data["Outcome"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    pred=model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

    result1 = ''
    if pred[0]:  # Corrected line
        result1 = "positive"
    else:
        result1 = "negative"

    return render(request, "predict.html", {"result2": result1})
