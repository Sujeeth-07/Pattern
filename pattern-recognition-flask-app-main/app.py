from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define the correct answer in the pattern sequence
correct_answer = "circle"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    user_answer = request.form.get("answer")

    if user_answer == correct_answer:
        message = "🎉 Well Done!"
        color = "green"
        gif_filename="Correct.gif"
    else:
        message = "❌ Try Again!"
        color = "red"
        gif_filename="Wrong.gif"

    return render_template("result.html", message=message, color=color,gif_filename=gif_filename)

if __name__ == "__main__":
    app.run(debug=True)
