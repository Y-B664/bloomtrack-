from flask import Flask, render_template
from app.routes.datasets import datasets_bluep

app=Flask(__name__)

app.register_blueprint(datasets_bluep)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
