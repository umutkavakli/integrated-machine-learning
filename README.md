# Integrated Machine Learning

An machine learning application that is integrated both desktop and web. Therefore, you can use it prompting with two files. The application calculates cost according to selected ML model with taken inputs.

<b>Inputs:</b>

- Sheet Thickness (mm)
- Yield Strength (mpa)
- Tensile Strength (mpa)
- Mold Weight (Tons)

<b>Output:</b>
- Cost (Euro per Ton)


<hr>

##### Models

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor
- SVM
- K-NN
<hr><br>


## Usage

To run app, start cloning repo into your local:
```
git clone https://github.com/umutkavakli/integrated-machine-learning.git
```
Move to project directory

```
cd integrated-machine-learning/
```

#### GUI

For desktop app:

```
python3 gui.py
```
<br>

![](gifs/gui.gif)

<br>

#### Web Server

For web server app:

```
python3 web.py
```

![](gifs/web.gif)