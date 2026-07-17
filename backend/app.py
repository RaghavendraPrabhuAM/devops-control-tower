from flask import Flask
from config import Config
from routes import api


app = Flask(__name__)

app.config["SECRET_KEY"] = Config.SECRET_KEY

app.register_blueprint(api)


if __name__ == "__main__":
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=True
    )