# 🧠 EmotiSense AI

EmotiSense AI is an emotion-aware journaling web application that analyzes user input and detects emotional patterns using AI.

---

## 🚀 Features

* 🔐 Login System (Username & Password)
* 🧠 Emotion Detection (Happy 😊, Sad 😔, Neutral 😐)
* ⚠️ Burnout Warning System
* 📊 Emotion Graph Visualization
* 🎨 Clean & User-Friendly Interface

---

## 🛠️ Technologies Used

* Python (Flask)
* TextBlob (Sentiment Analysis)
* HTML, CSS
* Chart.js
* Git & GitHub

---

## 📂 Project Structure

```
EmotiSense-AI/
│
├── app.py
├── users.txt
└── templates/
    ├── login.html
    └── index.html
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```
git clone https://github.com/sanikagundakar9-alt/EmotiSense-AI.git
```

2. Navigate to the project folder:

```
cd EmotiSense-AI
```

3. Install dependencies:

```
pip install flask textblob
```

4. Download TextBlob data:

```
python -m textblob.download_corpora
```

5. Run the application:

```
python app.py
```

6. Open in browser:

```
http://127.0.0.1:5000/
```

---

## 🔐 Default Login

Username:

```
admin
```

Password:

```
1234
```

---

## 📊 How It Works

* User logs into the system
* Writes daily thoughts in the journal
* AI analyzes the sentiment of the text
* Emotion is detected and displayed
* Graph updates in real-time
* Burnout warning is shown if negative emotions persist

---

## 🔮 Future Improvements

* More emotion categories (Anger, Anxiety, Excitement)
* Voice-based input
* Mobile app version
* Database integration
* Secure authentication system

---

## 🙌 Author

* Developed by Sanika Gundakar

---

## ⭐ Contribution

Feel free to fork this repository and improve it!

---

## 📜 License

This project is for educational purposes.
