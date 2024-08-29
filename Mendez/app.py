from flask import Flask, request, render_template
import re 

app = Flask(__name__)

def lexico(text):
    tokens = re.findall(r'\b\w+\b', text)
    return tokens
@app.route('/', methods= ['GET', 'POST'])
def indext():
    if request.method =='POST':
        text = request.form['text']   
        tokens = lexico(text)
        return render_template('index.html', tokens=tokens, text=text)
    return render_template('index.html' , tokens = None, text = None)
if __name__ == '__main__':
    app.run(debug=True)