from flask import Flask

server = Flask(__name__)


@server.route("/")
def hello():
    return "Ho ho ho"


@server.route("/day1")
def day1():
    return "Ho ho ho day1"


if __name__ == "__main__":
    server.run(host='0.0.0.0', port=80)
