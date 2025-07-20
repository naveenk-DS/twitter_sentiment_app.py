import streamlit as st
import re
import random

# Dummy model and vectorizer
class DummyModel:
    def predict(self, X):
        return [random.choice([0, 1, 2])]

class DummyVectorizer:
    def transform(self, X):
        return X

model = DummyModel()
vectorizer = DummyVectorizer()

def preprocess_tweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub(r'http\S+', '', tweet)
    tweet = re.sub(r'@\w+', '', tweet)
    tweet = re.sub(r'#\w+', '', tweet)
    tweet = re.sub(r'[^\w\s]', '', tweet)
    return tweet.strip()

st.title("Twitter Sentiment Analysis")
tweet = st.text_area("Enter a Tweet")

if st.button("Analyze"):
    if tweet.strip() == "":
        st.warning("Please enter a tweet.")
    else:
        cleaned_tweet = preprocess_tweet(tweet)
        vectorized_tweet = vectorizer.transform([cleaned_tweet])
        prediction = model.predict([vectorized_tweet])[0]

        if prediction == 0:
            sentiment = "Negative 😠"
        elif prediction == 1:
            sentiment = "Positive 😊"
        else:
            sentiment = "Neutral 😐"

        st.write(f"**Predicted Sentiment:** {sentiment}")
