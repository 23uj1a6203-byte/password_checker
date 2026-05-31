from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    suggestions = []

    if request.method == "POST":
        password = request.form["password"]

        if len(password) < 8:
            suggestions.append("Password should be at least 8 characters long")

        if not any(char.isdigit() for char in password):
            suggestions.append("Add at least one number")

        if not any(char.isupper() for char in password):
            suggestions.append("Add at least one uppercase letter")

        if not any(char in "!@#$%^&*" for char in password):
            suggestions.append("Add at least one special character")

        if len(suggestions) == 0:
            result = "Strong"
        elif len(suggestions) <= 2:
            result = "Medium"
        else:
            result = "Weak"

    return render_template(
        "index.html",
        result=result,
        suggestions=suggestions
    )

if __name__ == "__main__":
    app.run(debug=True)