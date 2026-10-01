from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load trained ML model
model = joblib.load("model .pkl")


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction
@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    study_hours = float(request.form["study_hours"])
    attendance = float(request.form["attendance"])
    previous_score = float(request.form["previous_score"])
    assignments_completed = float(request.form["assignments_completed"])
    sleep_hours = float(request.form["sleep_hours"])

    # Make prediction
    prediction = model.predict([[
        study_hours,
        attendance,
        previous_score,
        assignments_completed,
        sleep_hours
    ]])

    # Convert prediction into Pass/Fail
    if prediction[0] == 1:
        result = "Pass"
    else:
        result = "Fail"

    return jsonify({"prediction":result})


if __name__ == "__main__":
    app.run(debug=True)



