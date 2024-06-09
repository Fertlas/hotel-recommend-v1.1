from data_loader import load_data
from nlp_model import train_nlp_model
from chatbot import chat
import json
import pandas as pd

intents_file = 'intents.json'

# Load data
df = pd.read_csv('terengganuhotels.csv')

# Train NLP model
train_nlp_model(intents_file)

# Load intents
with open(intents_file) as file:
    intents = json.load(file)

# Start chat
chat(intents, df)
