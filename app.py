
from flask import Flask, render_template

app = Flask(__name__)

SAMPLE_TEXT = "Good typing is built through steady practice and careful attention. Focus on each word, keep a comfortable rhythm, and let accuracy guide your speed. Small improvements made every day can lead to confident and efficient typing.Go and Prastic daily"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test_page():
    return render_template('test.html', sample_text=SAMPLE_TEXT)

@app.route('/results')
def results_page():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
