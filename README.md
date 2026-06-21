# 🌱 Smart Crop Recommendation Engine – Agriculture

<div align="center">

### 🚀 Machine Learning Based Crop Recommendation System

Developed During Internship at **Innolift Ventures**

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Status](https://img.shields.io/badge/Status-Completed-success)

</div>

---

## 📖 Project Overview

The **Smart Crop Recommendation Engine – Agriculture** is a Machine Learning-powered web application developed as part of my internship at **Innolift Ventures**.

The primary objective of this project is to assist farmers and agricultural professionals in selecting the most suitable crop based on soil nutrients and environmental conditions.

The system analyzes key agricultural parameters such as Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH Level, and Rainfall, and then recommends the most appropriate crop using a trained Machine Learning model.

This project combines Machine Learning, Web Development, and Database Management to create an intelligent agricultural recommendation platform.

---

# 🎯 Problem Statement

Agriculture is one of the most important sectors for economic growth and food security. However, many farmers face challenges in selecting the most suitable crop due to variations in soil quality and climatic conditions.

Incorrect crop selection can lead to:

- Reduced agricultural productivity
- Poor crop yield
- Financial losses
- Inefficient use of resources

This project addresses these challenges by providing data-driven crop recommendations using Machine Learning.

---

# 💡 Proposed Solution

The Smart Crop Recommendation Engine predicts the most suitable crop based on:

- Soil Nutrient Levels
- Environmental Conditions
- Historical Agricultural Data

The recommendation helps users make informed farming decisions and improve productivity.

---

# ✨ Key Features

### 🌾 Crop Prediction

Predicts the most suitable crop using Machine Learning.

### 📊 Soil Analysis

Uses multiple soil nutrient parameters for prediction.

### 🌦 Environmental Analysis

Considers weather-related parameters such as temperature, humidity, and rainfall.

### 🖥 User-Friendly Interface

Simple and responsive web application developed using Flask.

### 🗄 Database Integration

Stores prediction records using SQLite.

### ⚡ Real-Time Results

Provides instant crop recommendations.

### 📱 Responsive Design

Accessible across desktops and laptops.

---

# 📊 Input Parameters

The system accepts the following inputs:

| Parameter | Description |
|------------|------------|
| Nitrogen (N) | Nitrogen content in soil |
| Phosphorus (P) | Phosphorus content in soil |
| Potassium (K) | Potassium content in soil |
| Temperature | Temperature in °C |
| Humidity | Relative humidity |
| pH | Soil pH value |
| Rainfall | Rainfall in mm |

---

# 🌱 Predicted Crops

The model can recommend crops such as:

- Rice
- Wheat
- Maize
- Cotton
- Banana
- Mango
- Papaya
- Watermelon
- Chickpea
- Coffee

and many more crops included in the dataset.

---

# 🛠 Technologies Used

## Frontend

- HTML5
- CSS3
- JavaScript

## Backend

- Python
- Flask

## Database

- SQLite

## Machine Learning

- Random Forest Classifier
- Scikit-Learn
- Pandas
- NumPy
- Joblib

## Version Control

- Git
- GitHub

---

# 🤖 Machine Learning Model

## Algorithm Used

### Random Forest Classifier

The Random Forest algorithm was selected because:

- High prediction accuracy
- Handles multiple features effectively
- Reduces overfitting
- Reliable for classification tasks
- Performs well on agricultural datasets

---

# 🔄 Machine Learning Workflow

### Step 1: Data Collection

Agricultural dataset collected containing soil and environmental parameters.

### Step 2: Data Preprocessing

- Data Cleaning
- Feature Selection
- Data Validation

### Step 3: Model Training

Random Forest Classifier was trained using the processed dataset.

### Step 4: Model Evaluation

Performance evaluated using training and testing datasets.

### Step 5: Model Saving

Model stored using:

- model.pkl
- label_encoder.pkl

### Step 6: Flask Integration

Machine Learning model integrated into the web application.

### Step 7: Database Integration

Prediction records stored in SQLite database.

### Step 8: Deployment Preparation

Project configured for deployment using:

- Procfile
- runtime.txt
- requirements.txt

---

# 📂 Project Structure

```text
Veltech-Summer-Internship/
│
├── static/
│   ├── css
│   ├── js
│   └── images
│
├── templates/
│   ├── index.html
│   ├── predict.html
│   ├── records.html
│   └── about.html
│
├── app.py
├── train_model.py
├── model.pkl
├── label_encoder.pkl
├── crop production.csv
├── requirements.txt
├── runtime.txt
├── Procfile
└── README.md
```

---

# 💻 System Requirements

## Hardware Requirements

- Intel Core i3 Processor or above
- Minimum 4 GB RAM
- 500 MB Storage
- Internet Connection

## Software Requirements

- Windows 10 / Windows 11
- Python 3.10+
- Visual Studio Code
- Git
- GitHub
- Google Chrome

---

# 📦 Required Python Libraries

Install all required packages using:

```bash
pip install -r requirements.txt
```

Main Libraries:

- Flask
- Pandas
- NumPy
- Scikit-Learn
- Joblib

---

# 📁 Required Files

The following files are essential for running the application:

| File Name | Purpose |
|------------|------------|
| app.py | Main Flask Application |
| model.pkl | Trained ML Model |
| label_encoder.pkl | Crop Label Decoder |
| train_model.py | Model Training Script |
| crop production.csv | Dataset |
| templates/ | HTML Templates |
| static/ | CSS, JS, Images |
| requirements.txt | Dependencies |
| Procfile | Deployment Configuration |
| runtime.txt | Runtime Configuration |

---

# ▶️ Installation Guide

## Clone Repository

```bash
git clone https://github.com/your-username/Veltech-Summer-Internship.git
```

## Navigate to Project Folder

```bash
cd Veltech-Summer-Internship
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
python app.py
```

## Open Browser

```text
http://127.0.0.1:5000
```

---

# 🎓 Internship Learning Outcomes

During this internship, I gained practical experience in:

✅ Machine Learning Development

✅ Flask Web Application Development

✅ Frontend Development using HTML, CSS, and JavaScript

✅ Database Management using SQLite

✅ Data Preprocessing and Feature Engineering

✅ Model Training and Evaluation

✅ Git and GitHub Version Control

✅ Project Documentation

✅ Debugging and Problem Solving

✅ Deployment Concepts

---

# 👨‍🏫 Mentor Guidance & Support

This project was successfully completed under the valuable guidance and mentorship of the Innolift Ventures team.

### Special Thanks To

**Mr. Venkatesh**
- Project Planning and Technical Guidance
- Development Workflow Support

**Mr. Akhil**
- Machine Learning and Application Integration Guidance

**Mr. Balakrishnan**
- Backend Development and Project Improvement Suggestions

**Ms. Jayasri**
- Project Reviews, Documentation Support, and Feedback

I sincerely thank all mentors for their continuous support, valuable feedback, and encouragement throughout this internship journey.

---

# 🏢 Internship Details

### Organization
Innolift Ventures

### Internship Domain
Machine Learning & Web Development

### Project Title
Smart Crop Recommendation Engine – Agriculture

### Internship Type
Summer Internship Program

### Duration
Successfully Completed

---

# 🏆 Project Outcome

Successfully designed and developed a complete Machine Learning-based Crop Recommendation System capable of providing intelligent crop suggestions based on soil and environmental parameters.

The project demonstrates practical implementation of:

- Machine Learning
- Flask Web Development
- Database Integration
- Agricultural Data Analysis
- Software Development Lifecycle
- Deployment Preparation

---

# 👨‍💻 Author

## R. Tarun

Bachelor of Technology in Computer Science and Engineering with Specialization in Artificial Intelligence and Machine Learning

Vel Tech Rangarajan Dr. Sagunthala R&D Institute of Science and Technology


### Connect With Me



🔗 LinkedIn:https://www.linkedin.com/in/tarun-r-b21a2a374 



## ⭐ If you found this project useful, please consider giving it a star on GitHub

### Thank You for Visiting This Repository 🚀
