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

## 📁 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/cart-abandonment-detector.git
cd cart-abandonment-detector
```

---

## 📦 Step 2: Install Required Libraries

```bash
pip install Flask
pip install numpy
pip install pandas
pip install scikit-learn
pip install matplotlib
```

---

## ✅ Step 3: Verify Installation (Optional)

```bash
python -c "import flask, numpy, pandas, sklearn, matplotlib; print('Libraries installed successfully!')"
```

---

## 🧠 Step 4: Train the Machine Learning Model

```bash
python train_model.py
```

> This generates and saves a trained `model.pkl` using **Random Forest Classifier**.

---

## 🚀 Step 5: Start the Flask App

```bash
python app.py
```

Then open your browser and go to:

```bash
http://127.0.0.1:5000/
```

---

## 🧪 Step 6: Try Sample Input

You’ll see a form with the following fields:

- 🕒 **Time on Site:** `4.2`
- 📄 **Pages Viewed:** `10`
- 💰 **Cart Value:** `180.0`

Click the **Predict** button.

---

### 🟢 Output Example:

```bash
✅ User is NOT likely to abandon the cart.
```

---

### 🔴 Output Example:

```bash
❌ User is LIKELY to abandon the cart.
```

---

## 🗂 Project Structure

```bash
cart-abandonment-detector/
├── cart_data.csv
├── generate_data.py
├── train_model.py        # Trains the Random Forest classifier
├── app.py                # Flask backend server
├── model.pkl             # Saved trained model
├── templates/
│   └── index.html        # Frontend form

```

---

## ⚙️ Model Details

- 🎯 **Algorithm Used:** Random Forest Classifier  
- 📊 **Target Variable:** `abandoned` (1 = abandoned, 0 = completed)  
- ✅ **Evaluation Metrics:** Accuracy, Precision, Recall, Confusion Matrix  
- 📄 **Data:** 1,000 synthetic user sessions

---

## 📌 Key Features Considered

- **Time on Site** (in minutes)  
- **Pages Viewed** (per session)  
- **Cart Value** (in dollars)

---

## 🌱 Future Scope

- Add features like device type, time of day, referral source  
- Integrate real-time session tracking  
- Use Streamlit for advanced UI  
- Add visual dashboards for business insights

---

## 👩‍💻 Authors

- 💡 Amrutha and Team  

---

## 📄 License

This project is for educational/demo purposes only.


