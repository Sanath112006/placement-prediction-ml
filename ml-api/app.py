from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

model = pickle.load(open("model.pkl","rb"))

# ✅ Home page
@app.route("/")
def home():
    return "ML Placement Prediction API is running 🚀"


# ✅ Prediction API
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        print("DATA:", data)

        cgpa = float(data["cgpa"])

        # 🔴 HARD RULE — CGPA eligibility
        if cgpa < 6.5:
            return jsonify({
                "prediction": "Not Placed",
                "confidence": 20,
                "cgpa_percent": round(cgpa * 10, 2),
                "reason": "CGPA below eligibility threshold"
            })

        # 👉 Prepare ML features
        features = [[
            cgpa,
            float(data["aptitude_score"]),
            float(data["communication_score"]),
            int(data["internships"]),
            int(data["projects"]),
            int(data["workshops"])
        ]]

        print("FEATURES:", features)

        # 👉 ML prediction + probability
        proba = model.predict_proba(features)[0][1]
        result = "Placed" if proba >= 0.5 else "Not Placed"

        # ⭐ CGPA placement strength logic
        if cgpa < 7:
            cgpa_percent = 55
        elif cgpa < 8:
            cgpa_percent = 70
        elif cgpa < 9:
            cgpa_percent = 85
        else:
            cgpa_percent = 95

        return jsonify({
            "prediction": result,
            "confidence": round(proba * 100, 2),
            "cgpa_percent": cgpa_percent
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)})


app.run(port=8000)