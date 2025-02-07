from flask import Flask, request, jsonify,render_template_string,render_template
import pickle
import re
import string
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


model = pickle.load(open('models/best_model.pkl', 'rb'))
vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))

app = Flask(__name__)

def predict_sentiment(text_review):
    def clean_text(text):
        text = re.sub(r'<.*?>', '', text)
        text=re.sub('[%s]'%re.escape(string.punctuation),'',text)
        text=re.sub('\w*\d\w*','',text)
        text = re.sub(r'\s+', ' ', text)
        text=re.sub('[''"",,,]','',text)
        text = text.lower().strip()
        return text

    cleaned_text = clean_text(text_review)
    vectorized_text = vectorizer.transform([cleaned_text])
    prediction = model.predict(vectorized_text)[0]

    return "Positive 😊" if prediction == 1 else "Negative 😞"



@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    review_text = ""  
    if request.method == "POST":
        review_text = request.form.get("text_review", "").strip()
        if review_text:
            sentiment = predict_sentiment(review_text)
    return render_template("index.html", sentiment=sentiment, review_text=review_text)



@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    review = data.get("text_review", "")
    if not review:
        return jsonify({"error": "No review provided"}), 400
    sentiment = predict_sentiment(review)
    return jsonify({"sentiment": sentiment})

if __name__ == "__main__":
    app.run()
