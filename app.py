from flask import Flask, render_template
from flask_pymongo import PyMongo
from config import Config
from db import init_db
from Routers.userRouter import user_bp

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(user_bp, url_prefix='/user')  

mongo = PyMongo(app)

init_db(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)