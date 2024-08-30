from flask import Flask, render_template, request
from functions import daryo_articles, daryo_article

app = Flask(__name__)

@app.route('/')
def index():
    articles = daryo_articles()
    return render_template('index.html', articles=articles)

@app.route('/article')
def article():
    title = request.args.get('title')
    url = request.args.get('url')
    image_link = request.args.get('image')
    article_data = daryo_article(title=title, link=url, image_link=image_link)
    return render_template('article.html', article=article_data)

if __name__ == "__main__":
    app.run(debug=True)
