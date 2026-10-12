
from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained machine learning model
with open("model/academic_advisor.pkl", "rb") as file:
    model = pickle.load(file)


# Generate advice based on the prediction
def get_advice(category):

    advice = {
        "Maintain Excellence": 
            "You are performing well. Maintain your study habits and continue aiming for academic excellence.",

        "Academic Improvement": 
            "You should improve your academic performance by attending lectures regularly and creating a consistent study timetable.",

        "Technical Development": 
            "Focus on improving your technical and mathematical skills through practice, tutorials and practical exercises.",

        "Intensive Academic Support": 
            "You may need additional academic support. Consider consulting your lecturers, attending tutorials and seeking help with difficult courses."
    }

    return advice.get(category, "Continue working towards your academic goals.")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    student_data = pd.DataFrame([{
        "cgpa": float(request.form["cgpa"]),
        "level": int(request.form["level"]),
        "failed_courses": int(request.form["failed_courses"]),
        "attendance": float(request.form["attendance"]),
        "study_hours": float(request.form["study_hours"]),
        "math_score": float(request.form["math_score"])
    }])

    prediction = model.predict(student_data)[0]

    advice = get_advice(prediction)

    return render_template(
        "index.html",
        prediction=prediction,
        advice=advice
    )


if __name__ == "__main__":
    app.run(debug=True)

#Flask(__name__) creates our web application.
#pickle.load() loads the machine learning model you trained in Google Colab.
#/ displays the website's homepage.
#/predict receives the student's information and sends it to the AI model.
#model.predict() produces a recommendation.
#get_advice() converts the recommendation into useful guidance.