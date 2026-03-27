import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Load saved model & vectorizer
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = [ps.stem(i) for i in text if i.isalnum() and i not in stopwords.words('english')]
    return " ".join(y)

import numpy as np
import nltk

def predict_mail(sample):
    processed = transform_text(sample)
    
    # TF-IDF features
    vector = tfidf.transform([processed]).toarray()
    
    # Extra features (same as training)
    extra = np.array([[len(sample), len(sample.split()), len(nltk.sent_tokenize(sample))]])
    
    # Combine
    final_input = np.hstack((vector, extra))
    
    # Prediction
    prob = model.predict_proba(final_input)[0]

    if prob[1] > 0.6:
        return f"🚨 SPAM ({prob[1]*100:.2f}%)"
    else:
        return f"✅ HAM ({prob[0]*100:.2f}%)"

# UI
st.title("📧 Email Spam Classifier")

input_msg = st.text_area("Enter Email Text")

if st.button("Check"):
    result = predict_mail(input_msg)
    st.success(result)