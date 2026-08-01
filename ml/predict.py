from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("course_ranker.pkl")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    similarity = data["similarity"]
    price = data["price"]
    course_type = data["type"]
    query_length = data["query_length"]
    title_length = data["title_length"]

    # Convert FREE/PAID to numeric
    if course_type == "FREE":
        course_type = 0
    else:
        course_type = 1

    X = pd.DataFrame([{
        "similarity": similarity,
        "price": price,
        "type": course_type,
        "query_length": query_length,
        "title_length": title_length
    }])

    probability = model.predict_proba(X)[0][1]

    prediction = model.predict(X)[0]

    return jsonify({
        "prediction": int(prediction),
        "recommendation_probability": float(probability)
    })


if __name__ == "__main__":
    app.run(port=5000, debug=True)