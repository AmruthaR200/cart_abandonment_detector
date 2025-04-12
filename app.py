from flask import Flask, request, render_template, redirect, url_for
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        if request.form.get("action") == "predict":
            time_on_site = float(request.form["time"])
            pages_viewed = int(request.form["pages"])
            cart_value = float(request.form["value"])

            features = np.array([[time_on_site, pages_viewed, cart_value]])
            prediction = model.predict(features)[0]

            result = "🛒 Likely to Abandon" if prediction == 1 else "✅ Likely to Checkout"

        elif request.form.get("action") == "clear":
            return redirect(url_for("index"))  # Just reload page to clear

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
