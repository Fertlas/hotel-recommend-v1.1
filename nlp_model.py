import json
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer # type: ignore
from sklearn.linear_model import LogisticRegression # type: ignore
import numpy as np
import pickle

lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens]
    return ' '.join(tokens)

def train_nlp_model(intents_file):
    with open(intents_file) as file:
        intents = json.load(file)
    
    sentences = []
    labels = []
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            sentences.append(preprocess_text(pattern))
            labels.append(intent['tag'])
    
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(sentences)
    y = np.array(labels)
    
    clf = LogisticRegression()
    clf.fit(X, y)
    
    with open('model.pkl', 'wb') as model_file:
        pickle.dump(clf, model_file)
    
    with open('vectorizer.pkl', 'wb') as vectorizer_file:
        pickle.dump(vectorizer, vectorizer_file)

def load_nlp_model():
    with open('model.pkl', 'rb') as model_file:
        clf = pickle.load(model_file)
    
    with open('vectorizer.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    
    return clf, vectorizer

def get_intent(text, clf, vectorizer):
    processed_text = preprocess_text(text)
    vectorized_text = vectorizer.transform([processed_text])
    intent = clf.predict(vectorized_text)[0]
    return intent
