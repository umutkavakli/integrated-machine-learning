from flask import Flask, request, render_template
import pandas as pd
import joblib

# Declare a Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    
    # If a form is submitted
    if request.method == 'POST':
        
        # Unpickle classifier
        model = joblib.load('models/model.pkl')
        
        # Get values through input bars
        sheet_value = request.form.get('sheet')
        yield_value = request.form.get('yield')
        tensile_value = request.form.get('tensile')
        mold_value = request.form.get('mold')
        
        # Put inputs to dataframe
        X = pd.DataFrame([[sheet_value, yield_value, tensile_value, mold_value]], columns = ['sheet-thickness', 'yield-strength', 'tensile-strength', 'mold-weight'])
        
        # Get prediction
        prediction = model.predict(X)[0]
        
    else:
        prediction = ""
        
    return render_template('index.html', output = prediction)


if __name__ == '__main__':
    app.run(debug = True)