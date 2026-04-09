from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    original_text = ""

    if request.method == 'POST':
        original_text = request.form['text']
        src = request.form['source']
        dest = request.form['target']

        translated_text = GoogleTranslator(source=src, target=dest).translate(original_text)

    return render_template('index.html',
                           translated_text=translated_text,
                           original_text=original_text)

if __name__ == '__main__':
    app.run(debug=True)