# SMART ACADEMIC ADVISOR SYSTEM

## 1. Introduction
The Smart Academic Advisor is an AI-powered web application designed to assist university students in making informed academic decisions. It analyses student academic information and generates personalised recommendations to improve academic performance.

## 2. Problem Statement
Many university students experience difficulties identifying their academic weaknesses, selecting areas to improve and maintaining satisfactory academic performance. Traditional academic advising may not always be immediately accessible. This project aims to develop an intelligent system that provides accessible, data-driven academic guidance.

## 3. Project Objectives
- To develop a web-based academic advising application.
- To collect and analyse student academic information.
- To apply Machine Learning techniques to academic recommendation.
- To identify students' academic strengths and weaknesses.
- To provide personalised academic recommendations.

## 4. Functional Requirements
- Accept student academic information.
- Accept CGPA and academic level.
- Analyse student information using a trained Machine Learning model.
- Generate academic recommendation categories.
- Display personalised recommendations.
- Provide an easy-to-use interface.

## 5. Non-Functional Requirements
- User-friendly interface.
- Reliable prediction results.
- Secure handling of student information.
- Maintainable software architecture.
- Compatibility with modern web browsers.

## 6. Development Methodology
The project adopts an iterative development approach. The development process includes requirements analysis, system design, dataset preparation, model development, implementation, integration and testing.

## 7. Artificial Intelligence Technique
The system uses Supervised Machine Learning through a Random Forest Classification algorithm. The model is trained using labelled academic data to predict appropriate academic recommendation categories.

## 8. Technologies
- Python
- Visual Studio Code
- Git and GitHub
- Google Colab
- Pandas and NumPy
- Scikit-learn
- Flask
- HTML and CSS

## 9. System Architecture
The student submits academic information through a Flask web interface. The application processes the information and sends it to a trained Machine Learning model saved as a Pickle (.pkl) file. The prediction is processed by the recommendation engine and displayed to the student.

## 10. Testing
The system will undergo unit testing, integration testing and functional testing to verify that its components work correctly and that valid academic recommendations are displayed.