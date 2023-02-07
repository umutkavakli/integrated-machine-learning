import pandas as pd
from flask import Flask, request, render_template
from model_loader import ModelLoader

# Declare a Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    # create instance of model loader
    model_loader = ModelLoader()

    # if a form is submitted
    if request.method == 'POST':
        
        # get values through input bars
        sheet_value = request.form.get('sheet')
        yield_value = request.form.get('yield')
        tensile_value = request.form.get('tensile')
        mold_value = request.form.get('mold')

        # get selected model from browser
        selected_model = request.form.get('model')

        # set model on model loader
        model_loader.set_model(selected_model)
        
        # put inputs to dataframe
        X = pd.DataFrame([[sheet_value, yield_value, tensile_value, mold_value]], columns = ['sheet-thickness', 'yield-strength', 'tensile-strength', 'mold-weight'])
        
        # get prediction
        prediction = model_loader.model.predict(X)[0]
    else:
        prediction = ""

    return render_template('index.html', output = prediction)


if __name__ == '__main__':
    app.run(debug = True)
    
    