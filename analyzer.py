from textblob import TextBlob

Get a sentence from the user
user_sentence = input("Enter a sentence to analyze: ")

Analyze the sentence provided by the user
text_to_analyze = TextBlob(user_sentence)

print("Sentiment Polarity: ", text_to_analyze.sentiment.polarity)
