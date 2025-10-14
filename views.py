
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')



# Create your views here.
from django.shortcuts import render
import numpy as np
import os
import joblib

# Load the trained model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'heart_disease_model.pkl')
model = joblib.load(model_path)

def predict(request):
    if request.method == "POST":
        # Get form data
        try:
            age = float(request.POST['age'])
            sex = float(request.POST['sex'])
            cp = float(request.POST['cp'])
            trestbps = float(request.POST['trestbps'])
            chol = float(request.POST['chol'])
            fbs = float(request.POST['fbs'])
            restecg = float(request.POST['restecg'])
            thalach = float(request.POST['thalach'])
            exang = float(request.POST['exang'])
            oldpeak = float(request.POST['oldpeak'])
            slope = float(request.POST['slope'])
            ca = float(request.POST['ca'])
            thal = float(request.POST['thal'])

            # Convert input into numpy array
            input_features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

            # Make prediction
            prediction = model.predict(input_features)[0]
            result = "High Risk of Heart Disease" if prediction == 1 else "Low Risk of Heart Disease"

        except ValueError:
            result = "Invalid input. Please enter valid numbers."

        return render(request, 'result.html', {'result': result})

    return render(request, 'predict.html')

