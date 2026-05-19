from flask import Flask, render_template_string, request

app = Flask(__name__)

questions = [
    {
        "question": "What is the capital of Myanmar?",
        "options": ["Yangon", "Mandalay", "Bagan", "Bago"],
        "answer": "Paris"
    },
    {
        "question": "Which language is used with Flask?",
        "options": ["Java", "Python", "C#", "PHP"],
        "answer": "Python"
    }
]
@app.route("/", methods=["GET", "POST"])
def quiz():
    score = None

    if request.method == "POST":
        score = 0

        for i, q in enumerate(questions):
            selected = request.form.get(f"q{i}")

            if selected == q["answer"]:
                score += 1

    return render_template_string(
        HTML_TEMPLATE,
        questions=questions,
        score=score,
        total=len(questions)
    )

if __name__ == "__main__":
    app.run(debug=True)
