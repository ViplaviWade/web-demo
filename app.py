from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def myapp():
    return render_template('index.html')

@app.route('/forsales')
def forsales():
    return render_template('forsales.html')

if __name__ == "__main__":
    app.run(debug=True)