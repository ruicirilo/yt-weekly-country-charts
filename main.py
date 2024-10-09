from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape')
def scrape():
    url = "https://kworb.net/youtube/insights/"
    response = requests.get(url)
    response.encoding = 'utf-8'  # Forçar a codificação para UTF-8
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontre a tabela
    table = soup.find('table')
    rows = table.find_all('tr')

    # Extraia os dados
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if cols:  # Verifique se a linha não está vazia
            data.append(cols)

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
