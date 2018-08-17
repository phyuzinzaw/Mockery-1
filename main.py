from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def indexenglish():
    return render_template('indexenglish.html')

@app.route('/fimage')
def fimage():
    return render_template('fimage.html')


@app.route('/simage')
def simage():
    return render_template('simage.html')

@app.route('/timage')
def timage():
    return render_template('timage.html')

@app.route('/taungyiparagraph')
def taungyiparagraph():
    return render_template('taungyiparagraph.html')

@app.route('/thadingyutparagraph')
def thadingyutparagraph():
    return render_template('thingyanparagraph.html')

@app.route('/thingyanparagraph')
def thingyanparagraph():
    return render_template('thadingyutparagraph.html')

if __name__ == '__main__':
    app.run(debug=True)
