import streamlit as st
import pickle
import re

# Load the trained model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ✅ Define the preprocessing function
def preprocess_tweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub(r'http\S+', '', tweet)
    tweet = re.sub(r'@\w+', '', tweet)
    tweet = re.sub(r'#\w+', '', tweet)
    tweet = re.sub(r'[^\w\s]', '', tweet)
    tweet = tweet.strip()
    return tweet

# ✅ Streamlit app layout
st.title("Twitter Sentiment Analysis")

tweet = st.text_area("Enter a Tweet")

# ✅ Only analyze when button is clicked
if st.button("Analyze"):
    if tweet.strip() == "":
        st.warning("Please enter a tweet.")
    else:
        cleaned_tweet = preprocess_tweet(tweet)
        vectorized_tweet = vectorizer.transform([cleaned_tweet])
        prediction = model.predict(vectorized_tweet)[0]

        # Convert prediction to label
        if prediction == 0:
            sentiment = "Negative 😠"
        elif prediction == 1:
            sentiment = "Neutral 😐"
        else:
            sentiment = "Positive 😊"

        st.write(f"**Predicted Sentiment:** {sentiment}")
