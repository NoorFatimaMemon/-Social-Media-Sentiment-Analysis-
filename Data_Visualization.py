import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import string 
import nltk
import json


class Visualization:
    def load_data(self, filename='Cleaned_text.json'):
        with open(filename, "w") as json_Cleaned_data:
            data = json.load(json_Cleaned_data)
        return data
    
    def main(self):
        try:
            # Read the JSON file into a DataFrame
            df = pd.read_json('Cleaned_text.json', lines=True)

            # Calculate the count of each sentiment value
            sentiment_counts = df['Sentiment'].value_counts()

            # Display the sentiment counts
            print(sentiment_counts)

        except Exception as e:
            print(e)


test = Visualization()
test.main()