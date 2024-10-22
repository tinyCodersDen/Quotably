import requests
from flask import Flask,render_template,request

app = Flask(__name__)

api_url2 = 'https://zenquotes.io/api/today'
response2 = requests.get(api_url2).json()[0]

quote = response2['q']
author = response2['a']

api_url3 = 'https://zenquotes.io/api/image'
response3 = requests.get(api_url3)

@app.route('/')
def home():
    return render_template('home.html',DailyQuote=quote,Author=author)

@app.route('/quotes',methods=['GET','POST'])
def quotes():
    category = request.form.get('category')
    if type(category)!=str:
        category = 'happiness'
    l = []
    api_url1 = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    for i in range(10):
        response1 = requests.get(api_url1, headers={'X-Api-Key': 'qUkBnMz5VG1gmaUy52kMZA==AKHKJpYyoaEtgrwK'})
        l.append([response1.json()[0]['quote'],response1.json()[0]['author']])
    if request.method=="POST":
        category = request.form.get('category')
        print(category)
        api_url1 = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
        l = []
        for i in range(10):
            response1 = requests.get(api_url1, headers={'X-Api-Key': 'qUkBnMz5VG1gmaUy52kMZA==AKHKJpYyoaEtgrwK'})
            l.append([response1.json()[0]['quote'],response1.json()[0]['author']])
        return render_template('quotes.html',quote1=l[0][0],author1=l[0][1],quote2=l[1][0],author2=l[1][1],quote3=l[2][0],author3=l[2][1],quote4=l[3][0],author4=l[3][1],quote5=l[4][0],author5=l[4][1],quote6=l[5][0],author6=l[5][1],quote7=l[6][0],author7=l[6][1],quote8=l[7][0],author8=l[7][1],quote9=l[8][0],author9=l[8][1],quote10=l[9][0],author10=l[9][1])
    if request.method=='GET':
        l = []
        for i in range(10):
            response1 = requests.get(api_url1, headers={'X-Api-Key': 'qUkBnMz5VG1gmaUy52kMZA==AKHKJpYyoaEtgrwK'})
            l.append([response1.json()[0]['quote'],response1.json()[0]['author']])
    return render_template('quotes.html',quote1=l[0][0],author1=l[0][1],quote2=l[1][0],author2=l[1][1],quote3=l[2][0],author3=l[2][1],quote4=l[3][0],author4=l[3][1],quote5=l[4][0],author5=l[4][1],quote6=l[5][0],author6=l[5][1],quote7=l[6][0],author7=l[6][1],quote8=l[7][0],author8=l[7][1],quote9=l[8][0],author9=l[8][1],quote10=l[9][0],author10=l[9][1])

@app.route('/random')
def random():
    return render_template('random.html', image_url = response3.url)

if __name__=='__main__':
    app.run(debug=True)