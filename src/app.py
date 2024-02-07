from flask import Flask
from build.run_build import build_application
from syntax.run_syntax import syntax_checker
from test.run_tests import run_tests

app = Flask(__name__)

app.add_url_rule('/build', 'build', build_application, methods=['POST'])
app.add_url_rule('/test', 'test', run_tests, methods=['POST'])
app.add_url_rule('/syntax', 'syntax', syntax_checker, methods=['POST'])


if __name__ == "__main__":
    app.run(debug=True, port=8024)
