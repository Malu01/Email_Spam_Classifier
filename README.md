
# 📧 Email Spam Classifier

## 🚀 Project Overview

The **Email Spam Classifier** is a Machine Learning-based system that automatically classifies messages as **Spam 🚨 or Ham ✅** using Natural Language Processing (NLP).

It analyzes the content of messages, extracts meaningful patterns, and predicts whether the message is spam. The project also includes an **interactive web application** built with Streamlit for real-time predictions.

## 🎯 Objectives

* Detect spam messages automatically
* Apply NLP techniques for text processing
* Train and evaluate multiple ML models
* Provide a real-time user interface for prediction

## ✨ Features

### 🔹 Core Features

* ✔️ Spam vs Ham classification
* ✔️ Text preprocessing (tokenization, stopword removal, stemming)
* ✔️ TF-IDF vectorization with n-grams
* ✔️ Feature engineering (text length, word count, sentence count)

### 🔹 Machine Learning Features

* ✔️ Multiple models (Naive Bayes, Logistic Regression, Random Forest)
* ✔️ Model comparison (Accuracy & Precision)
* ✔️ Confusion Matrix visualization
* ✔️ Reduced false positives & false negatives

### 🔹 Model Management

* ✔️ Model saving using `model.pkl`
* ✔️ Vectorizer saving using `vectorizer.pkl`
* ✔️ Fast loading without retraining

### 🔹 Web Application Features

* ✔️ Interactive UI using Streamlit
* ✔️ Real-time spam detection
* ✔️ Instant prediction output
* ✔️ Confidence score display

### 🔹 Visualization

* ✔️ WordCloud for spam keywords
* ✔️ Data distribution graphs

## 🛠️ Technologies Used

* **Language:** Python
* **Libraries:**

  * pandas, NumPy
  * scikit-learn
  * NLTK
  * Matplotlib, Seaborn
  * WordCloud
  * Streamlit

## 🧠 Machine Learning Models

* Naive Bayes
* Logistic Regression
* Random Forest

## 📊 Dataset

* UCI SMS Spam Collection Dataset
* Kaggle Spam Dataset
https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

## ⚙️ How It Works

### 1. Data Preprocessing

* Convert text to lowercase
* Remove stopwords
* Tokenization & stemming

### 2. Feature Extraction

* TF-IDF Vectorizer (with n-grams)
* Additional features:

  * Character count
  * Word count
  * Sentence count

### 3. Model Training

* Train-test split
* Train multiple models
* Evaluate performance

### 4. Prediction Pipeline

* Input text → preprocessing
* Convert using `vectorizer.pkl`
* Predict using `model.pkl`
* Display result
  
## 🌐 Web Application (Streamlit)

The application provides a simple interface where users can enter a message and get instant spam detection.

### ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🧪 Example

**Input:**

```text
Congratulations! You have won a free prize. Call now!
```

**Output:**

```text
🚨 SPAM (95%)
```
## 📈 Evaluation Metrics

* Accuracy
* Precision
* Confusion Matrix

---

## 🚀 Key Achievements

* Built a complete NLP-based spam detection system
* Achieved high accuracy with optimized models
* Developed a real-time prediction web app
* Improved model performance using feature engineering

## 📌 Conclusion

This project demonstrates how **Machine Learning + NLP + Web Application Development** can be combined to build a practical and efficient spam detection system.
