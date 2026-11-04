# Heart Disease Prediction System

A machine learning-based web application that predicts the likelihood of heart disease based on patient medical parameters.

## Technologies Used

- **Python** – Programming language
- **Django** – Backend framework
- **Scikit-learn** – Machine learning library
- **Logistic Regression** – Classification algorithm
- **Pandas** – Dataset handling
- **NumPy** – Numerical operations
- **Joblib** – Model serialization
- **HTML** – Frontend structure
- **CSS** – Frontend styling
- **JavaScript** – Frontend interactivity

## Project Workflow

1. Load the heart disease dataset using Pandas.
2. Separate input features and target variable.
3. Split the dataset into training and testing sets.
4. Train a Logistic Regression classification model.
5. Evaluate the model using accuracy score.
6. Save the trained model using Joblib.
7. Collect patient medical details through a web interface.
8. Process the inputs using Django and generate predictions.
9. Display the prediction result to the user.

## Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/kedarkhedkar18/Heart-Disease-Prediction-.git
```

**2. Navigate to the project folder**

```bash
cd Heart-Disease-Prediction-
```

**3. Install dependencies**

```bash
pip install django pandas numpy scikit-learn joblib
```

**4. Run the application**

```bash
python manage.py runserver
```

**5. Open in browser**

```text
http://127.0.0.1:8000/
```

## Disclaimer

This project is developed for educational purposes only. It is not intended to replace professional medical advice or diagnosis.
