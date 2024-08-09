from flask import Flask, render_template, request, send_file
import feedparser
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rss', methods=['GET', 'POST'])
def rss():
    rss_url = request.form['rss_url']
    feed = feedparser.parse(rss_url)

    titles = []
    links = []
    descriptions = []
    authors = []
    pubDates = []

    for entry in feed.entries:
        titles.append(entry.title)
        links.append(entry.link)
        descriptions.append(entry.description) 
        authors.append(entry.author)

    data = {'제목':titles, '링크':links, '요약':descriptions, '작성자': authors}
    df = pd.DataFrame(data)

    df.to_excel('result.xlsx', index=False)
    return render_template('result.html', rss_url=rss_url)

@app.route('/download_report')
def download_report():
    return send_file('result.xlsx', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)