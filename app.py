import streamlit as st

st.title("Twitter Sentiment Analysis")

tweet = st.text_area("Enter a Tweet")

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
