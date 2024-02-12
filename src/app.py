from flask import Flask
from build.run_build import build_application, build_results

app = Flask(__name__)

app.add_url_rule('/build', 'build', build_application, methods=['POST'])
app.add_url_rule('/output', 'output', build_results, methods=['GET'])


if __name__ == "__main__":
    app.run(debug=True, port=8024)
