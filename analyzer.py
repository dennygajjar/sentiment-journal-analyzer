from textblob import TextBlob

user_sentence = input("Enter a sentence you want to analyze: ")

text_to_analyze = TextBlob(user_sentence)
sentiment = text_to_analyze.sentiment

print("Sentiment Polarity:", sentiment.polarity)
