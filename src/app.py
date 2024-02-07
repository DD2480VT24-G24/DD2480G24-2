from flask import Flask
from build.run_build import build_application
from test.run_test import run_tests

app = Flask(__name__)

app.add_url_rule('/build', 'build', build_application, methods=['POST'])
app.add_url_rule('/test', 'test', run_tests, methods=['POST'])


if __name__ == "__main__":
    app.run(debug=True)
