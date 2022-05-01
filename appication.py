from flask import Flask

from config import config

app = Flask(__name__)


if __name__ == '__main__':
    app.config.from_abject(config['development'])
    app.run()
