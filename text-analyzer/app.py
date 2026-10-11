from flask import Flask, render_template, request, redirect, url_for
from collections import Counter
import os

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html', title = 'Home')

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/post', methods = ['GET', 'POST'])
def post():
    if request.method == 'GET':
        return render_template('post.html', title = 'Post')
    elif request.method == 'POST':
        content = request.form['content']
        word_count = len(content.split())
        char_count = len(content)
        sentence_count = content.count('.') + content.count('!') + content.count('?')
        clean_words=[word.strip('.,!?;()[]') for word in content.lower().split()]
        word_freqs = Counter(clean_words)
        word_frequency = word_freqs.most_common(10)
        return render_template('result.html',
                               title='Results',
                               content=content,
                               word_count=word_count,
                               char_count=char_count,
                               sentence_count=sentence_count,
                               freq=word_frequency)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)