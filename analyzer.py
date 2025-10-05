from textblob import TextBlob

text_to_analyze = TextBlob("I am feeling happy and excited to start my first project!")

sentiment = text_to_analyze.sentiment

print("Text: ", text_to_analyze)
print("Sentiment Polarity: ", sentiment.polarity)