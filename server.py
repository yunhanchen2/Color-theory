from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


questions = [
    {"type": "mcq", "question": "Which is a warm color?", "options": ["Blue", "Orange", "Green"], "answer": "Orange"},
    {"type": "mcq", "question": "Complement of red?", "options": ["Green", "Blue", "Cyan"], "answer": "Green"},
    {"type": "mcq", "question": "Primary color?", "options": ["Purple", "Yellow", "Black"], "answer": "Yellow"},
    {"type": "mcq", "question": "Which is a cool color?", "options": ["Red", "Orange", "Blue"], "answer": "Blue"},
    {"type": "mcq", "question": "Neutral color?", "options": ["Gray", "Pink", "Violet"], "answer": "Gray"},
    {"type": "drag", "question": "Monochromatic---Saturation", "correct": "blue"},
    {"type": "drag", "question": "Triadic", "correct": "orange"},
    {"type": "drag", "question": "Create your own color combination!", "correct": "purple"},
]


# ROUTES

@app.route('/')
def home():
   return render_template('home.html')


@app.route('/tutorial')
def tutorial():
   return render_template('tutorial.html')


@app.route('/quiz')
def quiz_start():
    return render_template('quiz.html', qnum=0, questions=questions)

@app.route('/quiz/<int:qnum>')
def quiz_question(qnum):
    return render_template('quiz.html', qnum=qnum, questions=questions)
    
if __name__ == '__main__':
   app.run(debug=True, port=5001)