from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

WORDS = {
    'noun': '(missing noun)',
    'verb': '(missing verb)',
    'place': '(missing place)',
    'adjective': '(missing adjective)',
    'plural_noun': '(missing plural noun)'
}
@app.route('/')
def madlib_form():
    return render_template('madlib_form.html')

@app.route('/story')
def generated_story():
    WORDS['noun'] = request.args.get('noun')
    WORDS['verb'] = request.args.get('verb')
    WORDS['place'] = request.args.get('place')
    WORDS['adjective'] = request.args.get('adjective')
    WORDS['plural_noun'] = request.args.get('plural_noun')
    story = Story(WORDS, """Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}.""")
    return render_template('story.html', new_story=story.generate())
