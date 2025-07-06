# Medical Insurance Cost Predictor

This project predicts **insurance charges** based on user input like age, BMI, smoker status, region, etc. It's built using **machine learning regression models** and deployed via a **Streamlit web app**.

![Python](https://img.shields.io/badge/python-v3.13+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.37+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

##  Project Structure

```
medical-insurance-predictor/
├── data/
│   └── cleaned.csv                 # Preprocessed dataset
│   └── random_forest.joblib        # Trained model (best performing)
├── notebook/
│   └── eda.ipynb                   # Exploratory Data Analysis
├── src/
│   └── preprocessing.ipynb         # Preprocessing + Feature Engineering
│   └── training.ipynb              # Model training & evaluation
├── streamlit/
│   └── app.py                      # Streamlit app
└── requirements.txt
```

##  Features

- EDA on medical cost data
- Feature Engineering: interaction terms like `smoker_bmi`
- Multiple regression models:
  - Linear
  - Ridge
  - Polynomial
  - Support Vector Regression (SVR)
  - Random Forest (Best Model)
- Log transformation on target to improve performance
- Deployed using Streamlit with user input controls

---

##  Model Performance

| Model | MAE | R² Score |
|-------|-----|----------|
| Linear Regression | 4,439 | 0.466 |
| Ridge Regression | 4,430 | 0.468 |
| Polynomial | 2,615 | 0.831 |
| SVR | 4,819 | 0.256 |
| **Random Forest** | **2,036** | **0.867** |

---

##  How to Run

**Clone the repo**
```bash
git clone https://github.com/sarfraspc/medical-insurance-costs.git
cd medical-insurance-costs
```

**Install dependencies**
```bash
pip install -r requirements.txt
```

**Launch the app**
```bash
cd streamlit
streamlit run app.py
```

---

##  Input Features

- **age** – Age of the person
- **sex** – Male or Female
- **bmi** – Body Mass Index
- **children** – Number of children
- **smoker** – Yes or No
- **region** – US region (Northwest, Southeast, etc.)

---

##  App Preview

<img width="483" alt="Screenshot 2025-07-06 161839" src="https://github.com/user-attachments/assets/c7c254bd-bd72-42d7-b8db-5700e4adf060" />

<img width="769" alt="Screenshot 2025-07-06 161926" src="https://github.com/user-attachments/assets/4202f880-c599-4181-8820-4c80e02a6fe6" />

---

##  Notes

- The target variable (charges) was log-transformed during training. Predictions are exponentiated back using `np.expm1()`.
- Interaction features like `smoker_bmi` help model non-linear effects.

---

##  Author

**Sarfras**  
[LinkedIn](https://www.linkedin.com/in/your-profile)

##  License

MIT License
