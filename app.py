import numpy as np
from flask import Flask,request,render_template
import pickle
app=Flask(__name__)
model=pickle.load(open('models/model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/questions')
def questions():
    return render_template('questions.html')

@app.route('/predict', methods=['POST'])
def predict():
    pclass = int(request.form['Pclass'])
    sex = request.form['Sex']
    age = float(request.form['Age'])
    sibsp = int(request.form['SibSp'])
    parch = int(request.form['Parch'])
    fare = float(request.form['Fare'])

    sex_encoded = 0 if sex == 'male' else 1
    final_features = [pclass, sex_encoded, age, sibsp, parch, fare]

    prediction = model.predict([final_features])
    output = round(prediction[0], 2)

    if output==1:
        return render_template('questions.html', prediction_text='Yes,you will survive the Titanic!')
    else:
        return render_template('questions.html', prediction_text='No, you will not survive the Titanic!')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)