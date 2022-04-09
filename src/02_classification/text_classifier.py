import re
import pandas as pd
import pickle as pkl
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

from flask import Flask, jsonify, request

# df = pd.read_csv("https://raw.githubusercontent.com/futurexskill/ml-model-deployment/main/Restaurant_Reviews.tsv.txt", sep="\t")
# ps = PorterStemmer()
# corpus = []

# for i in range(len(df)):
#     customer_review = re.sub("[^a-zA-Z]", ' ', df["Review"][i])
#     customer_review = customer_review.lower().split()
#     clean_review = [ps.stem(word) for word in customer_review if not word in set(stopwords.words("english"))]
#     clean_review = ' '.join(clean_review)
#     corpus.append(clean_review)

# # print(json.dumps(corpus, indent=4))
# vectorizer = TfidfVectorizer(max_features=1500, min_df=3, max_df=0.6)
# X = vectorizer.fit_transform(corpus).toarray().tolist()
# y = df.iloc[:, 1].values.tolist()
# # print(X)
# # print(y)

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

# # # Train the model
# classifierKNN = KNeighborsClassifier(n_neighbors=5, metric="minkowski", p=2)
# classifierKNN.fit(X_train, y_train)

# # # Test the model
# y_pred = classifierKNN.predict(X_train)
# print(accuracy_score(y_train, y_pred))
# print(confusion_matrix(y_train, y_pred))
# y_pred = classifierKNN.predict(X_test)
# print(accuracy_score(y_test, y_pred))
# print(confusion_matrix(y_test, y_pred))

# # # Prediction
# sample = ["Good batting by England", "bad performance by India in the match"]
# sample = vectorizer.transform(sample).toarray().tolist()
# sentiment = classifierKNN.predict(sample)
# print(sentiment)

# # Save the trained model
# pkl.dump(classifierKNN, open("models/text_classifier.pkl", "wb"))
# pkl.dump(vectorizer, open("models/tfidfmodel.pkl", "wb"))

# Flask API
app = Flask(__name__)
classifierKNN = pkl.load(open("src/model.pkl", "rb"))
vectorizer = pkl.load(open("src/vectorizer.pkl", "rb"))

@app.route('/sentiment/predict', methods=['POST'])
def sentiment_predict():
    json_data = request.get_json(force=True)
    try:
        output = {"sentiments": []}
        sentences = json_data['sentences']
        if type(sentences) == str:
            print(sentences)
            output["sentiments"].append({"message": sentences, "sentiment": None})
        elif type(sentences) == list:
            for sentence in sentences:
                print(sentence)
                output["sentiments"].append({"message": sentence, "sentiment": None})
        return jsonify({"message": sentences})
    except Exception:
        print(json_data)
        return jsonify({"message": "Invalid JSON"})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=80, debug=False)