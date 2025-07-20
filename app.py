import streamlit as st
import re
st.title("Twitter Sentiment Analysis")

tweet = st.text_area("Enter a Tweet")

# ✅ Define the preprocessing function
def preprocess_tweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub(r'http\S+', '', tweet)
    tweet = re.sub(r'@\w+', '', tweet)
    tweet = re.sub(r'#\w+', '', tweet)
    tweet = re.sub(r'[^\w\s]', '', tweet)
    tweet = tweet.strip()
    return tweet

if st.button("Analyze"):
   if tweet.strip() == "":
        st.warning("Please enter a tweet.")
   else:
        cleaned_tweet = preprocess_tweet(tweet)  # 👈 Now it works
        vectorized_tweet = vectorizer.transform([cleaned_tweet])
        prediction = model.predict(vectorized_tweet)[0]

        # Optional: Convert prediction to label
        if prediction == 0:
            sentiment = "Negative 😠"
        elif prediction == 1:
            sentiment = "Neutral 😐"
        else:
            sentiment = "Positive 😊"

        st.write(f"**Predicted Sentiment:** {sentiment}")
