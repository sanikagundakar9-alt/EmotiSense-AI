from flask import Flask, render_template, request, redirect, session
from textblob import TextBlob
import datetime

app = Flask(__name__)
app.secret_key = "secret123"

entries = []

def detect_emotion(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.3:
        return "Happy 😊"
    elif polarity < -0.3:
        return "Sad 😔"
    else:
        return "Neutral 😐"

def check_burnout(entries):
    recent = entries[-5:]
    sad_count = sum(1 for e in recent if "Sad" in e["emotion"])

    if sad_count >= 3:
        return "⚠️ You seem stressed lately!"
    return None

def get_counts(entries):
    happy = sum(1 for e in entries if "Happy" in e["emotion"])
    sad = sum(1 for e in entries if "Sad" in e["emotion"])
    neutral = sum(1 for e in entries if "Neutral" in e["emotion"])
    return happy, sad, neutral

def check_login(username, password):
    with open("users.txt", "r") as f:
        for line in f:
            user, pwd = line.strip().split(",")
            if user == username and pwd == password:
                return True
    return False

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if check_login(username, password):
            session["user"] = username
            return redirect("/home")

    return render_template("login.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    if "user" not in session:
        return redirect("/")

    warning = None

    if request.method == "POST":
        text = request.form["entry"]
        emotion = detect_emotion(text)
        date = datetime.datetime.now().strftime("%Y-%m-%d")

        entries.append({
            "date": date,
            "text": text,
            "emotion": emotion
        })

        warning = check_burnout(entries)

    happy, sad, neutral = get_counts(entries)

    return render_template("index.html",
                           entries=entries,
                           warning=warning,
                           happy=happy,
                           sad=sad,
                           neutral=neutral)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)