# 🛍️ Cart Abandonment Detector

## Project Overview

This project predicts cart abandonment for an e-commerce platform using machine learning. By analyzing user behavior metrics such as time spent on the site, pages viewed, and cart value, it predicts the likelihood that a user will abandon their cart. The project uses the **Random Forest Classifier** model to make these predictions and is hosted on a Flask web application with a simple user interface.

---

## Features

- **User Inputs:**
  - Time on Site (in minutes)
  - Pages Viewed
  - Cart Value (in dollars)

- **Predictions:**
  - Based on the user inputs, the model predicts whether the cart is likely to be abandoned.

---

## Tech Stack

- **Backend:** Python (Flask)
- **Libraries:** Pandas, Scikit-learn, NumPy, Matplotlib
- **Frontend:** HTML, CSS (Flask templates)
- **Machine Learning Model:** Random Forest Classifier

---

## Installation

To run the project locally, follow these steps:

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/cart-abandonment-detector.git
cd cart-abandonment-detector

### Step 2: Install Required Libraries
```bash
pip install Flask
pip install numpy
pip install pandas
pip install scikit-learn
pip install matplotlib

### Step 3: verify installation(optional)
```bash
python -c "import flask, numpy, pandas, sklearn, matplotlib; print('Libraries installed successfully!')"

 ### Step 4:Run Model Training Script First
```bash
python train_model.py

### Step 5:Start Flask App to Serve Predictions
```bash
python app.py

This should start your Flask server. Open your browser and go to:
```bash
http://127.0.0.1:5000/

