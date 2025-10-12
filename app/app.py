from flask import Flask, render_template
from app.routes.datasets import datasets_bluep
from app.routes.analisis import analisis_bluep

app=Flask(__name__)

app.register_blueprint(datasets_bluep)
app.register_blueprint(analisis_bluep)



@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


