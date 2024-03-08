from nltk.tokenize import word_tokenize
from textblob import TextBlob
from nltk.corpus import stopwords
import pandas as pd
import re
import json
import warnings
warnings.filterwarnings("ignore", category = DeprecationWarning)

class Sentiment_Analysis:
    def data_dump(self, new_data, filename="Cleaned_text.json"):
        # Open the JSON file and update its content
        with open(filename, 'r+') as file:
            # Load existing data into a dictionary
            file_data = json.load(file)
            # Append new data to existing data
            file_data.append(new_data)
            # Set file's current position at offset
            file.seek(0)
            # Convert the combined data back to JSON format
            json.dump(file_data, file, indent=4)
            file.close() 

    def creating_file(self, filename="Cleaned_text.json"):
        with open(filename, "w") as outfile:
            outfile.write('[]')
            outfile.close()

    def data_cleaning(self, text):
        text = text.lower()

        # to remove username from the text
        text = re.sub('@[^\s]+','',text)

        # to remove link from the text
        text = re.sub("(http\S+)", "", text)

        # to remove hashtags from the text
        text = re.sub(r'#(\w+)', "", text)

        # to remove the "rt" from the tweet text
        text = re.sub(r'^rt\s+', "", text)

        # to remove special characters from the text
        text = re.sub( r'[^a-zA-Z\s]', '', text)

        return text
    
    def sentiment_analysis(self, text):
        # Handle missing values and create a cleaned review text
        text = text if pd.notna(text) else ''
        stop_words = set(stopwords.words('english'))
        _text_tokens_ = word_tokenize(text)
        filtered_tweet_text = ' '.join([word for word in _text_tokens_ if word.lower() not in stop_words])

        # Analyze sentiment of the cleaned review text
        sentiment = TextBlob(filtered_tweet_text).sentiment.polarity

        return filtered_tweet_text, sentiment
    
    def main(self):
        self.creating_file()
        df = pd.read_csv('tweets.csv', encoding='cp1252')
        df = df['text']
        text_list = df.values.tolist()

        # Iterate through each review element in the list
        for text_index, text in enumerate(text_list):
            CleanedText = self.data_cleaning(text)
            CleanedTweet, sentiment = self.sentiment_analysis(CleanedText)

            # Create a new data entry with cleaned review text, verification status, and sentiment
            cleaned_data = [{"Index": text_index, 'CleanedTweet': CleanedTweet, 'Sentiment': sentiment}]              
            self.data_dump(new_data=cleaned_data)


test = Sentiment_Analysis()
test.main()  

    