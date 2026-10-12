# Smart Academic Advisor (SAA)

An AI-powered academic advising web application that analyses student academic information and provides personalised academic recommendations.

## Project Overview

The Smart Academic Advisor is a web-based system developed to demonstrate how Artificial Intelligence and Machine Learning can support academic advising.

Students enter information about their academic performance, and the system uses a trained Random Forest classification model to predict an academic recommendation category.

The system then displays appropriate guidance based on the prediction.

## Live Application

**Access the deployed application here:**

https://academic-advisor-etwi.onrender.com

## Objectives

- Demonstrate the application of Artificial Intelligence in academic advising.
- Use Machine Learning to classify student academic performance.
- Provide recommendations based on student academic information.
- Develop and deploy a functional web application.
- Apply software engineering practices, including version control and documentation.

## Features

- Student academic information input.
- Machine Learning-based prediction.
- Four academic recommendation categories:
  - Maintain Excellence
  - Academic Improvement
  - Technical Development
  - Intensive Academic Support
- Personalised academic guidance.
- Responsive web interface.
- Online deployment.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data handling |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning |
| Random Forest | Classification algorithm |
| Pickle | Saving and loading the trained model |
| Flask | Web application framework |
| HTML | Web page structure |
| CSS | User interface styling |
| Git | Version control |
| GitHub | Source code hosting |
| Render | Web application deployment |
| Google Colab | Model development and training |

## Student Input Features

The system uses the following information:

1. CGPA
2. Academic level
3. Number of failed courses
4. Attendance percentage
5. Daily study hours
6. Mathematics score

## Machine Learning Approach

A Random Forest Classifier was used to develop the prediction model.

The model was trained using a synthetic dataset containing 1,000 student records. The dataset was divided into training and testing sets to evaluate the model.

After training, the model was saved as `academic_advisor.pkl` and integrated into the Flask application.

**Note:** The dataset contains artificially generated sample records rather than real university student records. Therefore, the system is an academic demonstration and should not be treated as a validated institutional advising tool.

## Project Structure

```text
smart-academic-advisor/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── Procfile
│
├── model/
│   └── academic_advisor.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── docs/
    ├── system_design.md
    └── testing_report.md
```

The `docs` files should be included once created.

## How to Run the Project Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Enter the project directory

```bash
cd smart-academic-advisor
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment (Windows)

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

### 7. Open the application

Visit:

```text
http://127.0.0.1:5000
```

## Deployment

The application is deployed using Render and connected to its GitHub repository.

**Live URL:** https://academic-advisor-etwi.onrender.com

## Limitations

- The current model uses synthetic data rather than real student records.
- Prediction quality has not been validated using real university academic data.
- The recommendations are general guidance and do not replace professional academic advising.
- Further development would require anonymised institutional data, additional testing, and validation.

## Future Improvements

- Integration with a university student database.
- Student login and account management.
- More detailed academic performance analysis.
- Course-specific recommendations.
- Improved model training using validated academic data.
- An administrative dashboard for academic advisers.

## Author

Developed as a Computer Science academic project to demonstrate the integration of Machine Learning, software engineering, and web application development.