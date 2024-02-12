from flask import Flask
from build.run_build import build_application, test_results

app = Flask(__name__)

app.add_url_rule('/build', 'build', build_application, methods=['POST'])
app.add_url_rule('/output', 'build', test_results, methods=['GET'])


if __name__ == "__main__":
    app.run(debug=True, port=8024)
