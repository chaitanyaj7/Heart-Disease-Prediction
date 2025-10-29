# Heart-Disease-Prediction
Heart Disease Prediction using Machine Learning (Logistic Regression, SVM, KNN, Decision Tree) — built with Python, Scikit-Learn, and Streamlit to predict the likelihood of heart disease based on clinical parameters.
Aurthor - Chaitanya Jamdar 
# ❤️ Heart Disease Prediction Using Machine Learning

This project aims to predict the likelihood of **heart disease** in patients using machine learning algorithms.  
Multiple models were evaluated — **Logistic Regression**, **Support Vector Machine (SVM)**, **K-Nearest Neighbors (KNN)**, and **Decision Tree** — to identify the most accurate one.  
After testing and comparing results, **Logistic Regression** was selected as the final model due to its simplicity, interpretability, and strong performance.

---

## 🚀 Features
- Predicts heart disease based on user input parameters.  
- Compares multiple ML models for performance.  
- Interactive web interface built using **Streamlit**.  
- Preprocessed and scaled data for accurate results.  

---

## 🧩 Machine Learning Models Used
| Algorithm | Description | Accuracy |
|------------|--------------|-----------|
| Logistic Regression | Best performing model | ⭐ Highest |
| Support Vector Machine (SVM) | Non-linear classifier | Moderate |
| K-Nearest Neighbors (KNN) | Distance-based model | Moderate |
| Decision Tree | Rule-based learner | Moderate |

---

## 🧠 Tech Stack
- **Python**  
- **Pandas, NumPy, Scikit-learn**  
- **Matplotlib, Seaborn**  
- **Streamlit** (for frontend)  

---

## ⚙️ How It Works
1. **Data Preprocessing** – Clean and scale the dataset.  
2. **Model Training** – Train models using ML algorithms.  
3. **Model Evaluation** – Compare models using accuracy, precision, recall, and F1-score.  
4. **Deployment** – Deploy final Logistic Regression model via Streamlit app.  

---

## 🧾 Dataset
The dataset used contains health-related parameters such as:  
- Age  
- Sex  
- Chest Pain Type  
- Blood Pressure  
- Cholesterol  
- Fasting Blood Sugar  
- ECG results  
- Maximum Heart Rate  
- Exercise Induced Angina  
- Oldpeak, Slope, Major Vessels, Thalassemia  
- Target (1 = Disease, 0 = Healthy)  

---
## 🧮 Example Output
Input: Age=54, Cholesterol=240, MaxHR=160
Prediction: 1 → High chance of heart disease
---

## 🏁 Final Result
✅ **Logistic Regression achieved the best balance between accuracy and interpretability**, making it the final choice for deployment.

---

## 📦 Run Locally
```bash
git clone https://github.com/yourusername/heart-disease-prediction.git
cd heart-disease-prediction
pip install -r requirements.txt
streamlit run app.py
