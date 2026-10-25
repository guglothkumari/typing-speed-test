import random
from flask import Flask, render_template, request

app = Flask(__name__)

SAMPLE_TEXTS = [
    "The quick brown fox jumps over the lazy dog to test the typing speed and keyboard responsiveness.",
    "DevOps practices combine software development and IT operations to shorten the systems development life cycle.",
    "Containerization using Docker ensures that applications run reliably across different computing environments."
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test_page():
    text = random.choice(SAMPLE_TEXTS)
    return render_template('test.html', sample_text=text)

@app.route('/result', methods=['POST'])
def result():
    wpm = request.form.get('wpm', 0)
    accuracy = request.form.get('accuracy', 0)
    errors = request.form.get('errors', 0)
    return render_template('result.html', wpm=wpm, accuracy=accuracy, errors=errors)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)