import random
from nlp_model import get_intent, load_nlp_model
from recommendation_system import recommend_hotels

bot_name = "Mumei"

def get_response(intent, intents):
    for i in intents['intents']:
        if i['tag'] == intent:
            return random.choice(i['responses']), i.get('questions',[])

def chat(intents, df):
    clf, vectorizer = load_nlp_model()
    print("Hello! How can I help you today?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        
        intent = get_intent(user_input, clf, vectorizer)
        
        if intent == 'recommend_hotel':
            answers = []

            #find the dictionary for the recommend_hotel intent
            intent_dict = next((i for i in intents['intents'] if i['tag'] == intent), None)

            if intent_dict:
                questions = intent_dict.get('questions', [])

                for question in questions:
                    answer = input(f"Mumei-Bot: {question} ")
                    answers.append(answer)
            
            price_range, district, amenities = answers
            amenities = amenities.split(',')
            
            recommended_hotels = recommend_hotels(df, price_range, district,  amenities)
            if recommended_hotels.empty:
                print("Mumei-Bot: Sorry, no hotels match your criteria.")
            else:
                print("Mumei-Bot: Here are some hotels that match your criteria:")
                print(recommended_hotels[['Name', 'Room Rates', 'District', 'Room Types', 'Amenities']])
        else:
            response, _ = get_response(intent, intents)
            print(f"Mumei-Bot: {response}")

