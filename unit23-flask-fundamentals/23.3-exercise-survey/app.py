from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False



responses = []
curr_question = 0

@app.route('/')
def start_page():
    survey_title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions

    return render_template("start.html", survey_title=survey_title, instructions=instructions)

@app.route('/question/<int:question_num>')
def start_survey(question_num):
    if not question_num == curr_question:
        flash('You have tried to acces an invalid question. Please answer the current question to continue.')
        return redirect(f'/question/{curr_question}')
    else:
        if len(responses) < len(satisfaction_survey.questions):
            question = satisfaction_survey.questions[question_num].question
            choices = satisfaction_survey.questions[question_num].choices
            return render_template('question.html', question=question,choices=choices)
        else:
            return redirect('/thank-you')

@app.route('/answer', methods=["POST"])
def add_answer():
    global curr_question 
    answer = request.form['option']

    # responses = session['responses']
    responses.append(answer)
    session['responses'] = responses

    curr_question += 1
    return redirect(f'/question/{curr_question}')

@app.route('/thank-you')
def say_thanks():
    return render_template('thanks.html')

@app.route('/new-survey', methods=["POST"])
def start_new_survey():
    global curr_question, responses

    curr_question = 0
    responses = []
    session['responses'] = []
    return redirect("/question/0")

@app.route('/restart')
def restart_survey():
    return redirect('/')
