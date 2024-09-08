from flask import Flask, render_template, request
import pandas as pd
import re

app = Flask(__name__)

# Load the CSV file
df = pd.read_csv('constitution_articles.csv')

# Function to search for articles related to the crime or keyword
def search_articles(crime):
    crime = crime.lower()
    results = []
    for index, row in df.iterrows():
        article_text = str(row['text'])  # Ensure the article text is a string
        if re.search(crime, article_text, re.IGNORECASE):
            results.append(f"{row['article']}: {row['text']}")
    return results

# Route for the homepage (with search form)
@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        # Get the keyword entered by the user through form data (not JSON)
        keyword = request.form.get('keyword')  # Expecting form data, not JSON
        if keyword:
            # Perform search
            results = search_articles(keyword)
    return render_template('index.html', results=results)

# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)
