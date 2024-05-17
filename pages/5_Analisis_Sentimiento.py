import streamlit as st
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Function to perform sentiment analysis using TextBlob
def analyze_sentiment_textblob(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Function to perform sentiment analysis using VaderSentiment
def analyze_sentiment_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    compound_score = scores['compound']
    if compound_score >= 0.05:
        return "Positive"
    elif compound_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Streamlit app
def main():
    st.title("Sentiment Analysis")

    st.header("TextBlob Sentiment Analysis")
    textblob_input = st.text_area("Enter text for sentiment analysis:")
    if st.button("Analyze Sentiment (TextBlob)"):
        if textblob_input:
            sentiment = analyze_sentiment_textblob(textblob_input)
            st.write(f"Sentiment: {sentiment}")

    st.header("VaderSentiment Analysis")
    vader_input = st.text_area("Enter your text for sentiment analysis:")
    if st.button("Analyze Sentiment (VaderSentiment)"):
        if vader_input:
            sentiment2 = analyze_sentiment_vader(vader_input)
            st.write(f"Sentiment: {sentiment2}")

if __name__ == "__main__":
    main()
