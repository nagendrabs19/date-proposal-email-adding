from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# ---------------- MAIL CONFIG ----------------

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'nagendrabs657@gmail.com'
app.config['MAIL_PASSWORD'] = 'timqxdhzdqjguwpi'

mail = Mail(app)

# ---------------- ROUTES ----------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/question")
def question():
    return render_template("question.html")


@app.route("/activity")
def activity():
    return render_template("activity.html")


@app.route("/date")
def date():
    return render_template("date.html")


@app.route("/final", methods=["POST"])
def final():

    date = request.form.get("date")
    time = request.form.get("time")

    msg = Message(
        subject="❤️ Someone Accepted Your Date!",
        sender=app.config['MAIL_USERNAME'],
        recipients=["YOUR_GMAIL@gmail.com"]
    )

    msg.body = f"""
Someone completed your Romantic Date Proposal!

Date: {date}
Time: {time}
"""

    mail.send(msg)

    return render_template("final.html")


if __name__ == "__main__":
    app.run(debug=True)